import struct
import os
import sys
from datetime import datetime
from collections import Counter

def parse_bmp_header(file_path):
    """
    解析BMP文件头和信息头，并提取所有使用的RGB颜色
    """
    try:
        with open(file_path, 'rb') as f:
            # 读取BMP文件头（14字节）
            file_header = f.read(14)
            if len(file_header) < 14:
                raise ValueError("文件太小，无法读取完整的BMP文件头")
            
            # 解析文件头
            signature = file_header[0:2]
            file_size = struct.unpack('<I', file_header[2:6])[0]
            data_offset = struct.unpack('<I', file_header[10:14])[0]
            
            # 检查是否为BMP文件
            if signature != b'BM':
                raise ValueError("不是有效的BMP文件")
            
            # 读取信息头（至少40字节）
            info_header = f.read(40)
            if len(info_header) < 40:
                raise ValueError("文件太小，无法读取完整的BMP信息头")
            
            # 解析信息头
            header_size = struct.unpack('<I', info_header[0:4])[0]
            width = struct.unpack('<i', info_header[4:8])[0]
            height = struct.unpack('<i', info_header[8:12])[0]
            planes = struct.unpack('<H', info_header[12:14])[0]
            bits_per_pixel = struct.unpack('<H', info_header[14:16])[0]
            compression = struct.unpack('<I', info_header[16:20])[0]
            image_size = struct.unpack('<I', info_header[20:24])[0]
            
            # 获取文件大小和修改时间
            file_stats = os.stat(file_path)
            actual_file_size = file_stats.st_size
            modified_time = datetime.fromtimestamp(file_stats.st_mtime)
            
            # 读取调色板（如果有）
            palette = []
            if bits_per_pixel <= 8:
                palette_size = 4 * (2 ** bits_per_pixel)
                palette_data = f.read(palette_size)
                for i in range(0, len(palette_data), 4):
                    if i + 3 < len(palette_data):
                        b, g, r, a = palette_data[i], palette_data[i+1], palette_data[i+2], palette_data[i+3]
                        palette.append((r, g, b))
            
            # 跳到像素数据开始位置
            f.seek(data_offset)
            
            # 读取像素数据并提取所有RGB颜色
            all_colors = set()
            unique_colors_counter = Counter()
            
            if bits_per_pixel == 24:  # 24位真彩色
                row_size = width * 3
                padding = (4 - (row_size % 4)) % 4
                
                for y in range(height):
                    row_data = f.read(row_size)
                    f.read(padding)  # 跳过填充字节
                    
                    for i in range(0, len(row_data), 3):
                        if i + 2 < len(row_data):
                            b, g, r = row_data[i], row_data[i+1], row_data[i+2]
                            color = (r, g, b)
                            all_colors.add(color)
                            unique_colors_counter[color] += 1
            
            elif bits_per_pixel == 32:  # 32位带Alpha通道
                for y in range(height):
                    for x in range(width):
                        pixel_data = f.read(4)
                        if len(pixel_data) == 4:
                            b, g, r, a = pixel_data
                            color = (r, g, b)
                            all_colors.add(color)
                            unique_colors_counter[color] += 1
            
            elif bits_per_pixel <= 8:  # 索引颜色
                row_size = width
                padding = (4 - (row_size % 4)) % 4
                
                for y in range(height):
                    row_data = f.read(row_size)
                    f.read(padding)  # 跳过填充字节
                    
                    for color_index in row_data:
                        if color_index < len(palette):
                            color = palette[color_index]
                            all_colors.add(color)
                            unique_colors_counter[color] += 1
            
            # 按使用频率排序颜色
            sorted_colors = sorted(unique_colors_counter.items(), key=lambda x: x[1], reverse=True)
            
            return {
                'file_path': file_path,
                'signature': signature.decode('ascii'),
                'declared_file_size': file_size,
                'actual_file_size': actual_file_size,
                'data_offset': data_offset,
                'header_size': header_size,
                'width': width,
                'height': height,
                'planes': planes,
                'bits_per_pixel': bits_per_pixel,
                'compression': compression,
                'compression_name': get_compression_name(compression),
                'image_size': image_size,
                'modified_time': modified_time,
                'file_size_match': file_size == actual_file_size,
                'color_depth': f"{bits_per_pixel} bits",
                'dimensions': f"{width} x {height} pixels",
                'total_colors': len(all_colors),
                'all_colors': sorted(all_colors),  # 按RGB值排序
                'color_usage': sorted_colors,      # 按使用频率排序
                'has_palette': bits_per_pixel <= 8,
                'palette': palette if bits_per_pixel <= 8 else []
            }
            
    except Exception as e:
        return {'error': f"解析错误: {str(e)}", 'file_path': file_path}

def get_compression_name(compression_code):
    """获取压缩方式的名称"""
    compression_names = {
        0: "BI_RGB (无压缩)",
        1: "BI_RLE8 (8位RLE编码)",
        2: "BI_RLE4 (4位RLE编码)",
        3: "BI_BITFIELDS (位域)",
        4: "BI_JPEG (JPEG压缩)",
        5: "BI_PNG (PNG压缩)",
        6: "BI_ALPHABITFIELDS (Alpha位域)"
    }
    return compression_names.get(compression_code, f"未知压缩方式 ({compression_code})")

def rgb_to_hex(rgb):
    """将RGB元组转换为十六进制格式"""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def print_bmp_info(info):
    """打印BMP文件信息和所有RGB颜色"""
    print("=" * 80)
    print(f"BMP文件详细分析: {os.path.basename(info['file_path'])}")
    print("=" * 80)
    
    if 'error' in info:
        print(f"错误: {info['error']}")
        return
    
    # 基础信息
    print("【文件基本信息】")
    print(f"文件路径: {info['file_path']}")
    print(f"文件类型: BMP ({info['signature']})")
    print(f"声明文件大小: {info['declared_file_size']} bytes ({info['declared_file_size']/1024:.2f} KB)")
    print(f"实际文件大小: {info['actual_file_size']} bytes ({info['actual_file_size']/1024:.2f} KB)")
    print(f"大小匹配: {'是' if info['file_size_match'] else '否'}")
    print(f"最后修改时间: {info['modified_time']}")
    print(f"数据偏移量: {info['data_offset']} bytes")
    print(f"信息头大小: {info['header_size']} bytes")
    print(f"图像尺寸: {info['dimensions']}")
    print(f"颜色深度: {info['color_depth']}")
    print(f"压缩方式: {info['compression_name']}")
    print(f"图像数据大小: {info['image_size']} bytes")
    print(f"总颜色数量: {info['total_colors']} 种")
    print(f"使用调色板: {'是' if info['has_palette'] else '否'}")
    
    print("\n" + "=" * 80)
    print("【所有使用的RGB颜色】")
    print("=" * 80)
    
    if info['total_colors'] == 0:
        print("未找到颜色数据")
        return
    
    # 按RGB值排序显示所有颜色
    print("按RGB值排序:")
    for i, color in enumerate(info['all_colors'], 1):
        hex_color = rgb_to_hex(color)
        print(f"{i:3d}. RGB({color[0]:3d}, {color[1]:3d}, {color[2]:3d})  {hex_color}")
    
    print("\n" + "=" * 80)
    print("【颜色使用频率统计】")
    print("=" * 80)
    
    # 显示前20个最常用的颜色
    print("使用频率最高的颜色 (前20个):")
    for i, (color, count) in enumerate(info['color_usage'][:20], 1):
        hex_color = rgb_to_hex(color)
        percentage = (count / (info['width'] * info['height'])) * 100
        print(f"{i:2d}. RGB({color[0]:3d}, {color[1]:3d}, {color[2]:3d})  {hex_color}  - 使用次数: {count:6d} ({percentage:6.2f}%)")
    
    # 如果有调色板，显示调色板信息
    if info['has_palette'] and info['palette']:
        print("\n" + "=" * 80)
        print("【调色板信息】")
        print("=" * 80)
        for i, color in enumerate(info['palette']):
            hex_color = rgb_to_hex(color)
            print(f"调色板[{i:3d}]: RGB({color[0]:3d}, {color[1]:3d}, {color[2]:3d})  {hex_color}")

def analyze_multiple_files(file_paths):
    """分析多个BMP文件"""
    for file_path in file_paths:
        if os.path.exists(file_path):
            info = parse_bmp_header(file_path)
            print_bmp_info(info)
            print("\n" + "=" * 80 + "\n")
        else:
            print(f"文件不存在: {file_path}")
            print()

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python bmp_color_analyzer.py <bmp文件1> [bmp文件2 ...]")
        print("示例: python bmp_color_analyzer.py image1.bmp image2.bmp")
        print("或者直接拖拽BMP文件到脚本上")
        return
    
    file_paths = sys.argv[1:]
    analyze_multiple_files(file_paths)

if __name__ == "__main__":
    main()