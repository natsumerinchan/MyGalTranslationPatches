from PIL import Image, ImageDraw, ImageFont
import os
import io
import struct

# 配置参数
IMAGE_SIZE = (128, 128)          # 图片尺寸
NAME_BOX_SIZE = (96, 25.9)       # 人名框尺寸（宽, 高）
NAME_BOX_COLOR = (39, 33, 28)    # 人名框颜色（使用原始文件的灰色）
FONT_FILE = "WenQuanYi.ttf"      # 字体文件路径
BASE_TEXT_SIZE = 20              # 基础字体大小
TARGET_SIZE = 65592              # 使用原始文件的大小65592字节

def create_exact_bmp(img):
    """
    创建与原始文件格式完全一致的BMP文件（32位，65592字节）
    """
    # 转换为RGBA模式（32位）
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # 获取图像数据
    pixels = list(img.getdata())
    width, height = img.size
    
    # 32位BMP每像素4字节，不需要行填充
    bytes_per_row = width * 4
    image_data_size = bytes_per_row * height
    
    # BMP文件头（14字节）
    file_header = struct.pack('<2sIHHI', 
                             b'BM',                    # 签名
                             TARGET_SIZE,              # 文件大小
                             0,                        # 保留1
                             0,                        # 保留2
                             54)                       # 数据偏移量
    
    # BMP信息头（40字节）
    info_header = struct.pack('<IIIHHIIIIII',
                              40,                      # 信息头大小
                              width,                   # 宽度
                              height,                  # 高度
                              1,                       # 平面数
                              32,                      # 每像素位数（32位RGBA）
                              0,                       # 无压缩
                              image_data_size,         # 图像数据大小
                              2834,                    # 水平分辨率
                              2834,                    # 垂直分辨率
                              0,                       # 使用的颜色数
                              0)                       # 重要颜色数
    
    # 构建图像数据（BGRA顺序）
    image_data = bytearray()
    for y in range(height - 1, -1, -1):  # BMP是从下到上存储的
        row_start = y * width
        row_end = row_start + width
        row_pixels = pixels[row_start:row_end]
        
        # 写入像素数据（BGRA顺序）
        for pixel in row_pixels:
            r, g, b, a = pixel
            image_data.extend([b, g, r, a])
    
    # 组合所有数据
    bmp_data = file_header + info_header + image_data
    
    # 确保文件大小精确匹配原始文件
    if len(bmp_data) < TARGET_SIZE:
        # 填充到目标大小
        padding = TARGET_SIZE - len(bmp_data)
        bmp_data += b'\x00' * padding
    elif len(bmp_data) > TARGET_SIZE:
        # 截断到目标大小
        bmp_data = bmp_data[:TARGET_SIZE]
    
    return bmp_data

def get_bold_font(font_path, size):
    """获取加粗字体效果"""
    try:
        font = ImageFont.truetype(font_path, size)
        return font
    except IOError:
        return ImageFont.load_default()

def adjust_font_size_to_fit(draw, text, font_path, max_width, max_height, initial_size):
    """调整字体大小以确保文本不超出指定范围"""
    size = initial_size
    font = get_bold_font(font_path, size)
    
    while size > 8:
        font = get_bold_font(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        if text_width <= max_width and text_height <= max_height:
            return font, size
        
        size -= 1
    
    return get_bold_font(font_path, 8), 8

def draw_bold_text(draw, position, text, font, fill_color):
    """绘制加粗文本"""
    x, y = position
    offsets = [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
    
    # 加粗背景使用深灰色
    for offset in offsets:
        draw.text(offset, text, font=font, fill=(30, 25, 20, 255))
    
    # 前景文本
    if len(fill_color) == 3:
        fill_color = fill_color + (255,)
    draw.text(position, text, font=font, fill=fill_color)

def create_name_image(output_path, name, text_color):
    # 创建新图像（RGBA模式，32位）
    img = Image.new('RGBA', IMAGE_SIZE, (0, 0, 0, 0))  # 完全透明背景
    draw = ImageDraw.Draw(img)
    
    # 计算人名框的位置
    box_x = (IMAGE_SIZE[0] - NAME_BOX_SIZE[0]) / 2
    box_y = (IMAGE_SIZE[1] - NAME_BOX_SIZE[1]) / 2
    
    # 绘制人名框（使用原始文件的灰色，完全不透明）
    draw.rectangle(
        [box_x, box_y, box_x + NAME_BOX_SIZE[0], box_y + NAME_BOX_SIZE[1]],
        fill=NAME_BOX_COLOR + (255,)
    )
    
    # 调整字体大小
    font, actual_size = adjust_font_size_to_fit(
        draw, name, FONT_FILE, 
        NAME_BOX_SIZE[0] - 4,
        NAME_BOX_SIZE[1] - 4,
        BASE_TEXT_SIZE
    )
    
    if actual_size < BASE_TEXT_SIZE:
        print(f"提示: 文本'{name}'字体大小调整为 {actual_size}")
    
    # 计算文本位置
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = box_x + (NAME_BOX_SIZE[0] - text_width) / 2
    text_y = box_y + (NAME_BOX_SIZE[1] - text_height) / 2
    
    # 绘制文本
    draw_bold_text(draw, (text_x, text_y), name, font, text_color)
    
    # 创建与原始文件格式一致的BMP文件
    bmp_data = create_exact_bmp(img)
    
    # 保存文件
    with open(output_path, 'wb') as f:
        f.write(bmp_data)
    
    # 验证文件大小
    final_size = os.path.getsize(output_path)
    if final_size == TARGET_SIZE:
        print(f"成功生成: {output_path} ({final_size/1024:.2f}KB) - 文本: '{name}'")
        return True
    else:
        print(f"错误: 文件大小 {final_size/1024:.2f}KB != {TARGET_SIZE/1024:.2f}KB")
        return False

def main():
    # 检查字体文件
    if not os.path.exists(FONT_FILE):
        print(f"警告: 字体文件 {FONT_FILE} 不存在")
    
    # 读取name.txt文件
    try:
        with open("name.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("错误: name.txt 文件未找到")
        return
    
    success_count = 0
    total_count = 0
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        total_count += 1
        parts = line.split('\t')
        if len(parts) < 2:
            continue
        
        filename = parts[0] + ".bmp"
        name = parts[1]
        
        if len(parts) >= 3:
            try:
                color_str = parts[2].replace('(', '').replace(')', '')
                color_parts = color_str.split(',')
                if len(color_parts) == 3:
                    text_color = tuple(map(int, color_parts))
                else:
                    text_color = (255, 255, 255)
            except:
                text_color = (255, 255, 255)
        else:
            text_color = (255, 255, 255)
        
        if create_name_image(filename, name, text_color):
            success_count += 1
    
    print(f"\n生成完成: {success_count}/{total_count} 个文件成功生成")
    print(f"文件格式: 32位BMP，大小: {TARGET_SIZE} bytes")
    print(f"使用的人名框颜色: RGB{NAME_BOX_COLOR}")

if __name__ == "__main__":
    main()