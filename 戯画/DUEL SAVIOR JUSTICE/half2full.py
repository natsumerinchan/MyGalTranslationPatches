import re
import json
import os
import sys
import argparse
from pathlib import Path

def half_to_full(char):
    """
    将半角字符转换为全角字符
    """
    # 半角字符范围
    if 33 <= ord(char) <= 126:  # 可打印ASCII字符
        return chr(ord(char) + 65248)  # 转换为全角
    elif ord(char) == 32:  # 空格
        return chr(12288)  # 全角空格
    else:
        return char  # 其他字符保持不变

def convert_to_full_width(text):
    """
    将文本中的半角字符转换为全角字符
    """
    return ''.join(half_to_full(c) for c in text)

def clean_message(message):
    """
    清理message中的特殊标记：将不符合正则表达式的内容转换为全角字符
    """
    if not isinstance(message, str):
        return message
    
    # 定义正则表达式模式（匹配所有特殊标记）
    patterns = [
        r'@g.{1}',      # @g后跟任意一个字符
        r'@f[0-9]{2}',  # @f后跟两位数字
        r'@m[0-9]{2}',  # @m后跟两位数字
        r'@w[0-9]{4}',  # @w后跟四位数字
        r'@t[0-9]{4}',  # @t后跟四位数字
        r'@h[0-9]{4}[A-Z]{2}',      # @h后跟四位数字和两个大写字母
        r'@s[0-9]{4}',  # @s后跟四位数字
        r'@hA[0-9]{3}[A-Z]{2}',     # @hA后跟三位数字和两个大写字母
        r'@h[0-9]{4}T2',            # @h后跟四位数字和T2
        r'@o[0-9]{3}[a]{0,1}',
        r'@v[0-9]{10}[0-9a-z]{0,1}', 
        r'@v[0-9]{10}',           # @v后跟十位数字
        r'@v[a-z]{3}[0-9]{7}',            # @v后跟四个字母六位数字
        r'@v[a-z]{4}[0-9]{6}[a-z0-9]{0,1}',            # @v后跟四个字母六位数字
        r'@v[0-9]{2}[a-z]{1}',
        r'@v[0-9]{2,3}',
        r'@a',          # @a
        r'@c',          # @e
        r'@e',          # @e
        r'@k',          # @k
        r'@p',          # @p
        r'@n'           # @n
    ]
    
    # 合并所有模式
    pattern = '|'.join(patterns)
    
    # 查找所有特殊标记的位置
    matches = list(re.finditer(pattern, message))
    
    if not matches:
        # 如果没有特殊标记，将整个字符串转换为全角
        return convert_to_full_width(message)
    
    # 构建结果字符串
    result = []
    last_end = 0
    
    for match in matches:
        # 添加特殊标记前的文本（转换为全角）
        before_text = message[last_end:match.start()]
        result.append(convert_to_full_width(before_text))
        
        # 添加特殊标记本身（保持不变）
        result.append(match.group())
        
        last_end = match.end()
    
    # 添加最后一个特殊标记后的文本（转换为全角）
    after_text = message[last_end:]
    result.append(convert_to_full_width(after_text))
    
    return ''.join(result)

def process_json_object(obj):
    """
    处理单个JSON对象
    """
    if isinstance(obj, dict):
        # 处理message字段
        if 'message' in obj:
            obj['message'] = clean_message(obj['message'])
        # 处理name字段（转换为全角）
        if 'name' in obj:
            obj['name'] = convert_to_full_width(obj['name'])
        # 递归处理所有值
        for key, value in obj.items():
            obj[key] = process_json_object(value)
    elif isinstance(obj, list):
        # 处理列表中的每个元素
        for i in range(len(obj)):
            obj[i] = process_json_object(obj[i])
    return obj

def process_json_file(input_path, output_path=None):
    """
    处理单个JSON文件
    """
    try:
        # 读取JSON文件
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 处理数据
        processed_data = process_json_object(data)
        
        # 确定输出路径
        if output_path is None:
            output_path = input_path
        
        # 写入处理后的数据
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=2, ensure_ascii=False)
        
        print(f"处理完成: {input_path} -> {output_path}")
        return True
        
    except Exception as e:
        print(f"处理文件 {input_path} 时出错: {e}")
        return False

def process_directory(input_dir, output_dir=None):
    """
    递归处理目录中的所有JSON文件
    """
    input_path = Path(input_dir)
    
    # 如果没有指定输出目录，则原地处理（覆盖原文件）
    if output_dir is None:
        output_dir = input_dir
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    processed_count = 0
    error_count = 0
    
    # 递归查找所有JSON文件
    for json_file in input_path.rglob('*.json'):
        try:
            # 计算相对路径
            relative_path = json_file.relative_to(input_path)
            
            if output_dir == input_dir:
                # 原地处理
                output_file = json_file
            else:
                # 保持目录结构
                output_file = Path(output_dir) / relative_path
                output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 处理文件
            if process_json_file(str(json_file), str(output_file)):
                processed_count += 1
            else:
                error_count += 1
                
        except Exception as e:
            print(f"处理文件 {json_file} 时出错: {e}")
            error_count += 1
    
    print(f"\n处理完成！")
    print(f"成功处理: {processed_count} 个文件")
    print(f"处理失败: {error_count} 个文件")

def main():
    """
    主函数：处理命令行参数
    """
    parser = argparse.ArgumentParser(description='递归处理文件夹中的JSON文件，将message字段中不符合特殊标记模式的文本和name字段转换为全角字符')
    parser.add_argument('input_dir', help='输入文件夹路径')
    parser.add_argument('-o', '--output', help='输出文件夹路径（可选，默认为原地处理）')
    parser.add_argument('--backup', action='store_true', help='创建备份（原地处理时有效）')
    
    args = parser.parse_args()
    
    # 检查输入目录是否存在
    if not os.path.exists(args.input_dir):
        print(f"错误：输入目录 '{args.input_dir}' 不存在")
        sys.exit(1)
    
    # 如果是原地处理且需要备份
    if args.output is None and args.backup:
        backup_dir = Path(args.input_dir).parent / f"{Path(args.input_dir).name}_backup"
        import shutil
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        shutil.copytree(args.input_dir, backup_dir)
        print(f"已创建备份到: {backup_dir}")
    
    # 处理目录
    process_directory(args.input_dir, args.output)

if __name__ == "__main__":
    main()