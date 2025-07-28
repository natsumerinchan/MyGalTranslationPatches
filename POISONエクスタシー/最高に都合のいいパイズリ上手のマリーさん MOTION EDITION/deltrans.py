import re
import os
import sys
import argparse

def remove_trans_blocks(content):
    """
    删除所有以[TransName开头、以[TransHitret]结尾的文本块
    """
    pattern = r"\[TransName.+?\].+?\[TransHitret.+?\][\n\r]*"
    return re.sub(pattern, "", content, flags=re.DOTALL)

def process_file(file_path):
    """处理单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = remove_trans_blocks(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"✅ 处理成功: {file_path}")
        return True
    
    except Exception as e:
        print(f"❌ 处理失败 {file_path}: {str(e)}")
        return False

def process_directory(directory, extensions=None):
    """递归处理目录中的所有文件"""
    count = 0
    success = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if extensions:
                ext = os.path.splitext(file)[1].lower()
                if ext not in extensions:
                    continue
            
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                count += 1
                if process_file(file_path):
                    success += 1
    
    print(f"\n处理完成: 共扫描 {count} 个文件，成功处理 {success} 个文件")

def main():
    parser = argparse.ArgumentParser(description='删除指定格式的文本块')
    parser.add_argument('path', help='要处理的文件或目录路径')
    parser.add_argument('--ext', nargs='*', default=['.wks'], 
                        help='要处理的文件扩展名 (默认: .wks)')
    args = parser.parse_args()
    
    target_path = args.path
    extensions = [ext.lower() for ext in args.ext]
    
    if not os.path.exists(target_path):
        print(f"错误: 路径 '{target_path}' 不存在")
        sys.exit(1)
    
    if os.path.isfile(target_path):
        # 处理单个文件
        process_file(target_path)
    elif os.path.isdir(target_path):
        # 处理整个目录
        print(f"开始处理目录: {target_path}")
        print(f"文件类型: {', '.join(extensions) if extensions else '所有文件'}")
        process_directory(target_path, extensions)
    else:
        print(f"错误: '{target_path}' 不是有效的文件或目录")
        sys.exit(1)

if __name__ == "__main__":
    main()