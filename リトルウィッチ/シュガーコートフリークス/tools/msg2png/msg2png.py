from PIL import Image, ImageDraw, ImageFont
import os

# ===== 配置区域 =====
font_path = "WenQuanYi.ttf"  # 文泉驿字体路径
base_font_size = 25          # 基础字号
output_dir = "output"        # 输出目录

# 颜色配置
text_color = (102, 204, 255) # 浅海蓝色
outline_color = (255, 255, 255)  # 白色描边
outline_width = 2            # 描边粗细

# 加粗参数
bold_offset = 1.2            # 加粗程度（1.0为不加粗）
bold_steps = 3               # 加粗渲染次数（越多越粗）

# ===== 函数定义 =====
def load_bold_font():
    """加载加粗字体（多级回退）"""
    try:
        # 尝试直接加载加粗版本
        try:
            return ImageFont.truetype(font_path, int(base_font_size * bold_offset), layout_engine=ImageFont.LAYOUT_BASIC)
        except:
            # 回退到普通字体+人工加粗
            return ImageFont.truetype(font_path, base_font_size)
    except OSError:
        return ImageFont.load_default()

def render_bold_text(draw, pos, text, font, fill):
    """渲染加粗文字效果"""
    x, y = pos
    # 多重偏移绘制实现加粗
    for i in range(bold_steps):
        offset = i * 0.5
        draw.text((x+offset, y+offset), text, fill=fill, font=font)
    # 中心主体
    draw.text(pos, text, fill=fill, font=font)

def calculate_text_size(draw, text, font):
    """计算加粗后的文字尺寸"""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0] + bold_steps
    text_height = bbox[3] - bbox[1] + bold_steps
    return text_width, text_height

# ===== 主流程 =====
try:
    # 准备输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 加载字体
    font = load_bold_font()
    if font.size != int(base_font_size * bold_offset):
        print("⚠️ 使用人工加粗效果（建议安装支持加粗的字体文件）")

    # 处理输入文件
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # 跳过空行和注释行（以###开头）
            if not line or line.startswith('###'):
                continue
            if '\t' not in line:
                continue

            filename, text = line.split('\t', 1)
            filename = filename.strip()
            
            # 创建临时图像计算文字尺寸
            with Image.new("RGBA", (1, 1)) as tmp_img:
                draw = ImageDraw.Draw(tmp_img)
                text_width, text_height = calculate_text_size(draw, text, font)
            
            # 创建画布（宽度和高度自适应）
            img_width = text_width + outline_width * 4
            img_height = text_height + outline_width * 4
            img = Image.new("RGBA", (img_width, img_height))
            draw = ImageDraw.Draw(img)
            
            # 计算居中位置
            x_offset = (img_width - text_width) // 2
            y_offset = (img_height - text_height) // 2
            
            # 绘制描边（加粗版）
            for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                render_bold_text(
                    draw,
                    (x_offset + dx*outline_width, y_offset + dy*outline_width),
                    text,
                    font,
                    outline_color
                )
            
            # 绘制主体文字（加粗版）
            render_bold_text(
                draw,
                (x_offset, y_offset),
                text,
                font,
                text_color
            )
            
            # 保存文件
            output_path = os.path.join(output_dir, f"{filename}.png")
            img.save(output_path)
            print(f"✅ 已生成: {output_path}")

    print("\n🎉 处理完成！")

except Exception as e:
    print(f"❌ 发生错误: {str(e)}")
    if 'font' not in locals():
        print("💡 字体建议：")
        print("1. 使用支持加粗的字体文件（如WenQuanYi-Bold.ttf）")
        print("2. 或安装系统字体包：sudo apt install fonts-wqy-zenhei")