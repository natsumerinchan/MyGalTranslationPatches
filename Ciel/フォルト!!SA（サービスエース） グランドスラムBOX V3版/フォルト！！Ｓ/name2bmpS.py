import sys
import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm

def find_font(font_name):
    """在系统中查找指定字体"""
    try:
        # 获取系统中所有可用字体
        fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')
        fonts.extend(fm.findSystemFonts(fontpaths=None, fontext='ttc'))
        
        # 查找包含指定名称的字体
        for font_path in fonts:
            if font_name.lower() in os.path.basename(font_path).lower():
                return font_path
        
        # 如果没找到，尝试常见的中文字体
        common_chinese_fonts = [
            "msyh.ttc",  # 微软雅黑
            "simhei.ttf",  # 黑体
            "simsun.ttc",  # 宋体
            "simkai.ttf",  # 楷体
        ]
        
        # 在Windows字体目录中查找常见字体
        windows_font_dir = "C:/Windows/Fonts/"
        for font_file in common_chinese_fonts:
            font_path = os.path.join(windows_font_dir, font_file)
            if os.path.exists(font_path):
                return font_path
                
        return None
    except Exception as e:
        print(f"查找字体时出错: {e}")
        return None

def create_names_bmp(names, font_path, output_path, width=208, height=48):
    """创建包含所有人名的BMP文件（Alpha通道透明，完全去掉垂直偏移）"""
    # 计算图像总高度（每行48像素）
    total_height = len(names) * height
    
    # 创建RGBA图像（完全透明背景）
    image = Image.new('RGBA', (width, total_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # 尝试加载字体
    try:
        if font_path:
            # 加载字体
            font = ImageFont.truetype(font_path, 30)
        else:
            raise IOError("未提供字体路径")
    except IOError:
        print("警告: 无法加载指定字体，尝试使用默认字体")
        try:
            font = ImageFont.load_default()
        except:
            font = ImageFont.load_default()
    
    # 绘制每个人名（白色文字，完全透明背景）
    for i, name in enumerate(names):
        name = name.strip()
        if not name:
            continue
            
        # 计算文本位置 - 完全去掉垂直偏移
        y_position = i * height
        
        try:
            bbox = draw.textbbox((0, 0), name, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # 计算位置 - 2像素左边距，完全去掉垂直偏移
            x = 2
            y = y_position  # 完全去掉垂直偏移，直接使用y_position
            
            # 绘制白色文本 - 使用轻微描边
            offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            
            for dx, dy in offsets:
                draw.text((x+dx, y+dy), name, font=font, fill=(255, 255, 255, 255))
            
            # 再绘制中心文本
            draw.text((x, y), name, font=font, fill=(255, 255, 255, 255))
                
        except Exception as e:
            print(f"绘制文本 '{name}' 时出错: {e}")
    
    # 保存为32位BMP文件（带Alpha通道）
    image.save(output_path, 'BMP')
    print(f"已生成: {output_path}，包含 {len(names)} 个人名")
    print(f"背景: 完全透明 (Alpha通道)")
    print(f"左边距: 2 像素")
    print(f"垂直位置: 完全去掉偏移 (y = y_position)")

def main():
    if len(sys.argv) != 2:
        print("用法: python script.py <txt文件路径>")
        sys.exit(1)
    
    txt_path = sys.argv[1]
    output_path = "name.bmp"  # 使用标准文件名
    
    # 查找字体
    font_name = "WenQuanYi Micro Hei"
    font_path = find_font(font_name)
    
    if font_path:
        print(f"找到字体: {font_path}")
    else:
        print("警告: 未找到文泉驿微米黑字体，将尝试使用其他字体")
        font_path = find_font("msyh") or find_font("simsun") or find_font("simkai")
        if font_path:
            print(f"使用替代字体: {font_path}")
        else:
            print("警告: 未找到任何中文字体，将使用默认字体")
            font_path = None
    
    # 读取人名文件
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            names = file.readlines()
    except UnicodeDecodeError:
        try:
            with open(txt_path, 'r', encoding='gbk') as file:
                names = file.readlines()
        except Exception as e:
            print(f"错误: 无法读取文件 {txt_path}: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"错误: 无法读取文件 {txt_path}: {e}")
        sys.exit(1)
    
    # 过滤空行
    names = [name.strip() for name in names if name.strip()]
    
    if not names:
        print("错误: 文件中没有有效的人名")
        sys.exit(1)
    
    total_height = len(names) * 48
    print(f"生成 {len(names)} 个人名，总高度: {total_height} 像素")
    
    # 生成Alpha通道透明版本
    create_names_bmp(names, font_path, output_path)
    
    print("\n生成完成！")
    print("使用Alpha通道透明背景")
    print("完全去掉垂直偏移 - 文字紧贴每行顶部")

if __name__ == "__main__":
    main()