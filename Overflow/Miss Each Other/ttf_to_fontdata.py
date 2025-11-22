#!/usr/bin/env python3
"""
TTF/OTF to FONTDATA.DAT Converter
Converts TrueType/OpenType fonts to FILMEngine.gem compatible FONTDATA.DAT format
Supports Unicode range: \u0000 to \uFFFF

Based on forum analysis:
- UTF-16 encoding for index table
- Each character uses 8 bytes (2 indices) in index table
- RLE compression for bitmap data
- Two textures per character: foreground and background (outline/shadow)
- Data starts at offset 0x80000
"""

import struct
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import sys

def rle_compress_4bit(pixels):
    """
    RLE compress 4-bit grayscale pixel data according to FILMEngine format
    
    Args:
        pixels: List of 4-bit grayscale values (0-15)
    
    Returns:
        Compressed bytes
    """
    compressed = []
    i = 0
    length = len(pixels)
    
    while i < length:
        # Count consecutive transparent pixels (0)
        if pixels[i] == 0:
            count = 0
            while i < length and pixels[i] == 0 and count < 0x7F:
                count += 1
                i += 1
            if count > 0:
                compressed.append(count)
        
        # Count consecutive non-transparent pixels
        else:
            current_value = pixels[i]
            count = 0
            while (i < length and pixels[i] == current_value and 
                   count < 8):  # Max 8 consecutive non-transparent pixels
                count += 1
                i += 1
            
            if count > 0:
                # Format: high 4 bits = count + 7, low 4 bits = grayscale value
                compressed_byte = ((count + 7) << 4) | current_value
                compressed.append(compressed_byte)
    
    # Add termination byte
    compressed.append(0x00)
    return bytes(compressed)

def create_character_textures(char, font, image_size=(32, 32)):
    """
    Create foreground and background textures for a character
    
    Args:
        char: Character to render
        font: PIL ImageFont object
        image_size: Size of output textures
    
    Returns:
        Tuple of (foreground_pixels, background_pixels) as 4-bit grayscale lists
    """
    # Create foreground (main character)
    fg_img = Image.new('L', image_size, 0)  # Black background
    fg_draw = ImageDraw.Draw(fg_img)
    
    # Get text bounding box to center the character
    try:
        bbox = fg_draw.textbbox((0, 0), char, font=font)
    except AttributeError:
        bbox = fg_draw.textsize(char, font=font)
        bbox = (0, 0, bbox[0], bbox[1])
    
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate centered position with punctuation adjustment
    x = (image_size[0] - text_width) / 2 - bbox[0]
    y = (image_size[1] - text_height) / 2 - bbox[1]
    
    # Adjust punctuation characters to appear lower
    punctuation_chars = {'.', '。', ',', '，', '、'}
    if char in punctuation_chars:
        x += 1
        y += 5  # Move punctuation down by 5 pixels
    
    # Draw foreground character (white)
    fg_draw.text((x, y), char, fill=255, font=font)
    
    # Create background (outline/shadow effect)
    bg_img = Image.new('L', image_size, 0)
    bg_draw = ImageDraw.Draw(bg_img)
    
    # Draw slightly offset and blurred for outline effect
    bg_draw.text((x+1, y+1), char, fill=128, font=font)  # Gray shadow
    bg_img = bg_img.filter(ImageFilter.GaussianBlur(0.5))
    
    # Convert to 4-bit grayscale (0-15)
    def to_4bit_grayscale(img):
        pixels = []
        for y in range(image_size[1]):
            for x in range(image_size[0]):
                # Convert 8-bit (0-255) to 4-bit (0-15)
                pixel_value = img.getpixel((x, y))
                if pixel_value > 0:
                    # Scale 1-255 to 1-15
                    scaled = max(1, min(15, pixel_value // 17))
                    pixels.append(scaled)
                else:
                    pixels.append(0)  # Transparent
        return pixels
    
    fg_pixels = to_4bit_grayscale(fg_img)
    bg_pixels = to_4bit_grayscale(bg_img)
    
    return fg_pixels, bg_pixels

def ttf_to_fontdata(ttf_path, output_path, font_size=28):
    """
    Convert TTF/OTF font to FONTDATA.DAT format with correct structure
    
    Args:
        ttf_path: Path to input TTF/OTF font file
        output_path: Path for output FONTDATA.DAT file
        font_size: Font size for rendering
    """
    
    # Check if font file exists
    if not os.path.exists(ttf_path):
        print(f"Error: Font file '{ttf_path}' not found")
        return False
    
    try:
        # Load font with specified size
        font = ImageFont.truetype(ttf_path, font_size)
        print(f"Loaded font: {ttf_path}")
    except Exception as e:
        print(f"Error loading font: {e}")
        return False
    
    # Initialize data structures
    index_table = [(0, 0)] * 65536  # 65536 entries, each 8 bytes (fg_offset, bg_offset)
    compressed_data = []  # Store all compressed texture data
    
    # Data starts at 0x80000 (524288 bytes)
    current_offset = 0x80000
    
    print("Rendering characters and compressing textures...")
    
    # Process each Unicode character from \u0000 to \uFFFF
    for char_code in range(0, 65536):
        try:
            char = chr(char_code)
            
            # Skip control characters (except space)
            if char_code < 0x20 and char_code != 0x20:
                continue
            
            # Create foreground and background textures
            fg_pixels, bg_pixels = create_character_textures(char, font)
            
            # RLE compress both textures
            fg_compressed = rle_compress_4bit(fg_pixels)
            bg_compressed = rle_compress_4bit(bg_pixels)
            
            # Store offsets in index table at the correct UTF-16 position
            fg_offset = current_offset
            bg_offset = current_offset + len(fg_compressed)
            
            index_table[char_code] = (fg_offset, bg_offset)
            compressed_data.append((char_code, fg_compressed, bg_compressed))
            
            current_offset += len(fg_compressed) + len(bg_compressed)
            
            # Progress indicator
            if char_code % 1000 == 0:
                print(f"Processed {char_code}/65536 characters...")
                
        except Exception as e:
            # Character not supported - index remains (0, 0)
            pass
    
    print(f"Rendering completed. {len([x for x in index_table if x != (0,0)])} characters generated.")
    
    # Write FONTDATA.DAT file
    try:
        with open(output_path, 'wb') as f:
            # 1. Write index table (65536 entries, each 8 bytes)
            # Format: [fg_offset][bg_offset] both as 4-byte little-endian integers
            for fg_offset, bg_offset in index_table:
                f.write(struct.pack('<I', fg_offset))
                f.write(struct.pack('<I', bg_offset))
            
            print(f"Written: 65536-entry index table ({65536 * 8} bytes)")
            
            # 2. Pad to 0x80000 if needed
            current_pos = f.tell()
            if current_pos < 0x80000:
                f.write(b'\x00' * (0x80000 - current_pos))
            
            # 3. Write compressed texture data in the correct order
            # We need to write the data in the order they appear in the index table
            # Create a mapping from offset to data
            data_map = {}
            for char_code, fg_data, bg_data in compressed_data:
                fg_offset = index_table[char_code][0]
                bg_offset = index_table[char_code][1]
                data_map[fg_offset] = fg_data
                data_map[bg_offset] = bg_data
            
            # Write data in increasing offset order
            sorted_offsets = sorted(data_map.keys())
            for offset in sorted_offsets:
                f.write(data_map[offset])
            
            total_compressed_size = sum(len(data_map[offset]) for offset in sorted_offsets)
            print(f"Written: {len(compressed_data)} character textures ({total_compressed_size} bytes compressed)")
            
            total_size = 0x80000 + total_compressed_size
            print(f"Total file size: {total_size} bytes ({total_size / 1024 / 1024:.2f} MB)")
        
        print(f"Successfully created: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        return False

def main():
    """Main function with command line interface"""
    if len(sys.argv) < 3:
        print("Usage: python ttf_to_fontdata.py <input_font.ttf> <output_fontdata.dat> [font_size]")
        print("Example: python ttf_to_fontdata.py simhei.ttf FONTDATA.DAT 28")
        sys.exit(1)
    
    ttf_path = sys.argv[1]
    output_path = sys.argv[2]
    font_size = int(sys.argv[3]) if len(sys.argv) > 3 else 28
    
    print("TTF/OTF to FONTDATA.DAT Converter")
    print("==================================")
    print(f"Input font: {ttf_path}")
    print(f"Output file: {output_path}")
    print(f"Font size: {font_size}")
    print(f"Character range: \\u0000 to \\uFFFF (65536 characters)")
    print()
    
    success = ttf_to_fontdata(ttf_path, output_path, font_size)
    
    if success:
        print("\nConversion completed successfully!")
    else:
        print("\nConversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
