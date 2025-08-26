import re
import json
import os
import sys
from pathlib import Path

def remove_ruby_annotations(text):
    """移除Ruby注音格式，但跳过文本为字母且注音为数字的情况"""
    pattern = re.compile(r'《(?P<文本>.+?):(?P<注音>.+?)》')
    
    def replace_func(match):
        text_part = match.group('文本')
        ruby_part = match.group('注音')
        # 跳过文本为字母且注音为数字的情况
        if text_part.isalpha() and ruby_part.isdigit():
            return match.group(0)  # 返回原始字符串
        return text_part  # 其他情况返回文本部分
    
    return pattern.sub(replace_func, text)

def process_json_file(file_path):
    """处理单个JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 递归处理JSON中的所有字符串
        def process_value(obj):
            if isinstance(obj, str):
                return remove_ruby_annotations(obj)
            elif isinstance(obj, dict):
                return {k: process_value(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [process_value(item) for item in obj]
            return obj
        
        processed_data = process_value(data)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        
        print(f"处理成功: {file_path}")
    except Exception as e:
        print(f"处理失败 {file_path}: {str(e)}")

def process_directory(directory):
    """处理目录下所有JSON文件"""
    if not os.path.isdir(directory):
        print(f"错误: 目录不存在 - {directory}")
        return
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.json'):
                file_path = Path(root) / file
                process_json_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python script.py <目录路径>")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    process_directory(target_directory)
    print("处理完成!")