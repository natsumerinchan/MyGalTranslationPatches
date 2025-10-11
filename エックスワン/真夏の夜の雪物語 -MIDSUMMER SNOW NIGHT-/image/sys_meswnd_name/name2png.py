import os
import json
from PIL import Image, ImageDraw, ImageFont
import re

def draw_rounded_rectangle(draw, x1, y1, x2, y2, radius, color):
    """
    绘制圆角矩形（辅助函数）
    """
    # 绘制四个角
    draw.ellipse([x1, y1, x1 + radius * 2, y1 + radius * 2], fill=color)  # 左上角
    draw.ellipse([x2 - radius * 2, y1, x2, y1 + radius * 2], fill=color)  # 右上角
    draw.ellipse([x1, y2 - radius * 2, x1 + radius * 2, y2], fill=color)  # 左下角
    draw.ellipse([x2 - radius * 2, y2 - radius * 2, x2, y2], fill=color)  # 右下角
    
    # 绘制矩形区域
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=color)  # 中间水平矩形
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=color)  # 中间垂直矩形

def create_text_image(text, filename, width, height, font_size=None, has_background=False):
    """
    创建文本图片
    :param has_background: 是否为true，如果是则显示灰色背景长条
    """
    try:
        # 自动计算合适的字体大小
        if font_size is None:
            base_size = max(12, min(36, height - 10))
            if len(text) > 4:
                font_size = max(12, base_size - 4)
            else:
                font_size = base_size
        else:
            font_size = max(12, min(font_size, height - 8))
        
        # 尝试使用系统中文字体
        font_paths = [
            "C:/Windows/Fonts/msyh.ttc",
            "C:/Windows/Fonts/simhei.ttf", 
            "C:/Windows/Fonts/simsun.ttc",
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/Hei.ttc",
            "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        ]
        
        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    font = ImageFont.truetype(font_path, font_size)
                    break
                except:
                    continue
        
        if font is None:
            font = ImageFont.load_default()
    except Exception as e:
        print(f"字体加载失败，使用默认字体: {e}")
        font = ImageFont.load_default()

    # 创建透明背景图片
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # 如果有背景，绘制灰色长条
    if has_background:
        # 灰色背景颜色
        bg_color = (128, 128, 128, 255)  # 灰色
        
        # 计算长条尺寸（比图片稍小，留出边距）
        bar_height = height - 6  # 上下各留3像素边距
        bar_width = width - 6    # 左右各留3像素边距
        
        # 计算长条位置（居中）
        bar_x = (width - bar_width) // 2
        bar_y = (height - bar_height) // 2
        
        # 绘制圆角矩形（两端弧线封闭）
        radius = bar_height // 2  # 圆角半径等于高度的一半，形成胶囊形状
        
        # 绘制圆角矩形
        draw_rounded_rectangle(draw, bar_x, bar_y, bar_x + bar_width, bar_y + bar_height, radius, bg_color)
    
    # 计算文本位置
    max_attempts = 3
    current_font_size = font_size
    
    for attempt in range(max_attempts):
        try:
            if attempt > 0:
                for font_path in font_paths:
                    if os.path.exists(font_path):
                        try:
                            font = ImageFont.truetype(font_path, current_font_size)
                            break
                        except:
                            continue
            
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            if text_width <= width - 10 and text_height <= height - 10:
                text_x = (width - text_width) // 2
                text_y = (height - text_height) // 2 - bbox[1]
                break
            else:
                current_font_size = max(12, current_font_size - 2)
                if attempt == max_attempts - 1:
                    text_x = 5
                    text_y = 5
        except:
            text_x = 10
            text_y = (height - current_font_size) // 2
            break

    # 绘制文字
    if has_background:
        # 灰色背景模式：白字黑边
        text_color = (255, 255, 255, 255)  # 白色文字
        border_color = (0, 0, 0, 255)      # 黑色边框
        border_width = 2
    else:
        # 正常模式：白字灰边
        text_color = (255, 255, 255, 255)  # 白色文字
        border_color = (80, 80, 80, 220)   # 灰色边框
        border_width = 1

    # 绘制文字边框
    for dx in range(-border_width, border_width + 1):
        for dy in range(-border_width, border_width + 1):
            if dx != 0 or dy != 0:
                try:
                    draw.text((text_x + dx, text_y + dy), text, font=font, fill=border_color)
                except:
                    pass
    
    # 绘制主文字
    try:
        draw.text((text_x, text_y), text, font=font, fill=text_color)
    except Exception as e:
        print(f"文本渲染失败: {text}, 错误: {e}")
        return False
    
    # 保存图片
    try:
        image.save(filename, 'PNG')
        bg_info = " [灰色背景]" if has_background else ""
        print(f"已生成: {filename} ({width}x{height}, '{text}'{bg_info})")
        return True
    except Exception as e:
        print(f"保存图片失败 {filename}: {e}")
        return False

def create_unified_mapping(image_info, input_contents):
    """
    统一的映射逻辑 - 同时支持顺序映射和ImageID映射
    """
    filename_map = {}
    
    # 从 input.txt 创建多种键的映射
    input_by_index = {}  # 按文件名中的数字索引
    input_by_imageid = {}  # 按ImageID
    
    for filename, text, has_background in input_contents:
        # 提取文件名中的数字作为索引
        numbers = re.findall(r'\d+', filename)
        if numbers:
            index_key = int(numbers[0])
            input_by_index[index_key] = (filename, text, has_background)
    
    # 处理所有Records
    for block_index, record in enumerate(image_info.get('Records', [])):
        image_id = record.get('ImageID')
        
        # 查找尺寸信息
        width, height = 100, 40
        for section in record.get('Sections', []):
            if section.get('Tag') == 'stdinfo' and section.get('Info'):
                info = section['Info']
                width = info.get('Width', width)
                height = info.get('Height', height)
                break
        
        # 确定输出文件名和文本 - 优先级顺序
        filename = None
        text = None
        has_background = False
        
        # 1. 首先尝试按block_index映射
        if block_index in input_by_index:
            filename, text, has_background = input_by_index[block_index]
        
        # 2. 如果上面失败，尝试按ImageID映射  
        if filename is None and image_id in input_by_index:
            filename, text, has_background = input_by_index[image_id]
        
        # 3. 如果都失败，使用默认值
        if filename is None:
            filename = f"image_{block_index:02d}_000"
            text = f"Text_{block_index:02d}"
            has_background = False
            print(f"警告: Block {block_index} (ImageID: {image_id}) 没有对应的输入文本，使用默认值")
        
        filename_map[block_index] = {
            'filename': filename + '.png',
            'width': width,
            'height': height,
            'image_id': image_id,
            'text': text,
            'has_background': has_background
        }
    
    return filename_map

def load_image_info(json_file='info.json'):
    """加载JSON文件"""
    if not os.path.exists(json_file):
        print(f"错误: 找不到 {json_file} 文件")
        return None
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"加载: {data.get('ImageBaseName', '未知')}, {len(data.get('Records', []))}个记录")
            return data
    except Exception as e:
        print(f"读取JSON文件失败: {e}")
        return None

def parse_input_file(input_file='input.txt'):
    """解析输入文件，支持第三个字段为true/false"""
    if not os.path.exists(input_file):
        print(f"错误: 找不到 {input_file} 文件")
        return None
    
    encodings = ['utf-8', 'gbk', 'shift_jis', 'cp932']
    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as f:
                lines = f.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        print("无法解码输入文件，尝试使用默认编码")
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    
    text_contents = []
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # 使用制表符分割
        parts = line.split('\t')
        
        if len(parts) >= 2:
            filename = parts[0].strip()
            text = parts[1].strip()
            
            # 检查是否有第三个字段（背景设置）
            has_background = False
            if len(parts) >= 3:
                bg_setting = parts[2].strip().lower()
                if bg_setting == 'true':
                    has_background = True
                    print(f"读取: {filename} -> '{text}' [灰色背景]")
                else:
                    print(f"读取: {filename} -> '{text}'")
            else:
                print(f"读取: {filename} -> '{text}'")
            
            if filename and text:
                text_contents.append((filename, text, has_background))
    
    return text_contents

def main():
    print("通用HG3图片生成工具 - 支持灰色背景")
    print("=" * 50)
    print("说明: input.txt每行格式: 文件名\t文本\t[true/false]")
    print("     第三个字段为true时显示灰色背景长条")
    print("=" * 50)
    
    # 解析输入文件
    text_contents = parse_input_file()
    if not text_contents:
        print("没有找到有效的文本内容")
        return
    
    print(f"\n总共读取了 {len(text_contents)} 个文本项")
    
    # 统计背景设置
    bg_count = sum(1 for _, _, has_bg in text_contents if has_bg)
    print(f"其中 {bg_count} 个设置了灰色背景")
    
    # 加载图片信息
    image_info = load_image_info()
    if not image_info:
        return
    
    # 使用统一的映射逻辑
    filename_map = create_unified_mapping(image_info, text_contents)
    
    # 检查映射完整性
    mapped_count = len(filename_map)
    input_count = len(text_contents)
    record_count = len(image_info.get('Records', []))
    
    print(f"\n映射统计:")
    print(f"  info.json记录数: {record_count}")
    print(f"  input.txt行数: {input_count}") 
    print(f"  成功映射数: {mapped_count}")
    
    if mapped_count != record_count:
        print(f"警告: 映射数量({mapped_count})与记录数量({record_count})不匹配!")
    
    # 显示映射详情
    print(f"\n映射详情:")
    for block_index, info in filename_map.items():
        mapping_type = "顺序映射" if block_index in [int(re.findall(r'\d+', info['filename'])[0])] else "ImageID映射"
        bg_info = " [灰色背景]" if info['has_background'] else ""
        print(f"  Block {block_index:2d}: {info['filename']} [{mapping_type}]{bg_info}")
        print(f"    ImageID: {info['image_id']}, 尺寸: {info['width']}x{info['height']}")
        print(f"    文本: '{info['text']}'")
    
    # 生成图片
    success_count = 0
    error_count = 0
    
    print(f"\n开始生成图片...")
    
    for block_index, info in filename_map.items():
        try:
            if create_text_image(
                info['text'], 
                info['filename'], 
                info['width'], 
                info['height'], 
                has_background=info['has_background']
            ):
                success_count += 1
            else:
                error_count += 1
        except Exception as e:
            print(f"生成图片失败 {info['filename']}: {e}")
            error_count += 1
    
    # 输出结果
    print(f"\n生成完成!")
    print(f"成功: {success_count}, 失败: {error_count}")
    
    # 统计背景图片数量
    bg_success = sum(1 for info in filename_map.values() if info['has_background'])
    print(f"其中灰色背景图片: {bg_success}个")
    
    if error_count == 0:
        print("所有图片生成成功！")
    else:
        print(f"有 {error_count} 个文件生成失败，请检查上述错误信息")

if __name__ == "__main__":
    main()