import re
import os
import sys

def is_kana_or_dot(line):
    """检查行是否只包含日文假名或・"""
    match = re.match(r'●(.+?)●(.+)', line)
    if not match:
        return False
    content = match.group(2)
    
    # 日文假名和・的Unicode范围
    hiragana_full = '\u3040-\u309F'  # 全角平假名
    katakana_full = '\u30A0-\u30FF'  # 全角片假名
    katakana_half = '\uFF65-\uFF9F'  # 半角片假名
    dot = '\u30FB'  # ・字符
    
    # 检查是否只有・
    if re.fullmatch(f'^[{dot}]+$', content):
        return True
    
    # 检查是否只有假名或假名+・
    kana_pattern = f'^[{hiragana_full}{katakana_full}{katakana_half}{dot}]+$'
    return bool(re.fullmatch(kana_pattern, content))

def is_kanji_only(line):
    """检查行是否只包含日文汉字和々"""
    match = re.match(r'●(.+?)●(.+)', line)
    if not match:
        return False
    content = match.group(2)
    # 日文汉字范围：\u4E00-\u9FAF，々是\u3005
    return all('\u4E00' <= char <= '\u9FAF' or char == '\u3005' for char in content)

def get_valid_lines(lines):
    """过滤掉○开头的行和空行，只返回●开头的行及其索引"""
    valid_lines = []
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('●') and not stripped.startswith('○'):
            valid_lines.append((idx, stripped))
    return valid_lines

def process_lines(lines):
    """处理文本行，添加<ruby>标签"""
    valid_lines = get_valid_lines(lines)
    
    for i in range(len(valid_lines)):
        current_idx, current_line = valid_lines[i]
        parts = current_line.split('●', 2)
        if len(parts) != 3:
            continue
            
        content = parts[2]
        # 检查是否只有・
        if re.fullmatch(r'^・+$', content):
            lines[current_idx] = f'{parts[0]}●{parts[1]}●<ruby>{content}\n'
            continue
            
        # 原有逻辑：假名行+汉字行
        if i < len(valid_lines) - 1:
            next_idx, next_line = valid_lines[i + 1]
            if is_kana_or_dot(current_line) and is_kanji_only(next_line):
                lines[current_idx] = f'{parts[0]}●{parts[1]}●<ruby>{content}\n'
    
    return lines

def process_file(file_path):
    """处理单个文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    processed_lines = process_lines(lines)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)
    print(f"处理完成: {file_path}")

def process_directory(directory):
    """处理目录下所有txt文件"""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(root, file)
                try:
                    process_file(file_path)
                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")

def main():
    if len(sys.argv) != 2:
        print("使用方法: python script.py <目录路径或文件路径>")
        print("示例: python script.py ./text_files")
        return
    
    target_path = sys.argv[1]
    
    if os.path.isfile(target_path) and target_path.lower().endswith('.txt'):
        process_file(target_path)
    elif os.path.isdir(target_path):
        process_directory(target_path)
    else:
        print("错误: 路径必须是目录或.txt文件")

if __name__ == "__main__":
    main()