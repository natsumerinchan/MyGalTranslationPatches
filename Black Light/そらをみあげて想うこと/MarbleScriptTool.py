import os
import sys
import argparse

def process_file(input_path, output_path=None, mode='forward'):
    """处理单个二进制文件，执行正向或反向替换"""
    if output_path is None:
        output_path = input_path
    
    with open(input_path, 'rb') as f:
        data = f.read()
    
    if mode == 'forward':
        # 正向处理：00 -> 0D0A，末尾0101 -> "#endline"
        modified_data = data.replace(b'\x00', b'\x0D\x0A')
        if modified_data.endswith(b'\x01\x01'):
            modified_data = modified_data[:-2] + b'#endline'
    else:
        # 反向处理：0D0A -> 00，"#endline" -> 0101（包括后面跟着的0D0A）
        modified_data = data
        
        # 先处理所有"#endline"及其后的0D0A
        endline_marker = b'#endline'
        endline_pos = modified_data.find(endline_marker)
        while endline_pos != -1:
            end_pos = endline_pos + len(endline_marker)
            # 查找后面连续的0D0A
            crlf_count = 0
            while end_pos + crlf_count + 1 < len(modified_data) and \
                  modified_data[end_pos + crlf_count:end_pos + crlf_count + 2] == b'\x0D\x0A':
                crlf_count += 2
            
            # 替换为0101（#endline本身对应一个0101，每对0D0A对应一个0101）
            replacement = b'\x01\x01' * (1 + crlf_count // 2)
            modified_data = modified_data[:endline_pos] + replacement + modified_data[end_pos + crlf_count:]
            
            # 继续查找下一个"#endline"
            endline_pos = modified_data.find(endline_marker, endline_pos + len(replacement))
        
        # 特殊处理文件末尾单独的#endline（没有后面跟着的0D0A的情况）
        if modified_data.endswith(endline_marker):
            modified_data = modified_data[:-len(endline_marker)] + b'\x01\x01'
        
        # 最后替换剩余的0D0A为00
        modified_data = modified_data.replace(b'\x0D\x0A', b'\x00')
    
    with open(output_path, 'wb') as f:
        f.write(modified_data)

def process_directory(directory, output_dir=None, mode='forward'):
    """处理目录中的所有文件"""
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            if output_dir:
                output_path = os.path.join(output_dir, filename)
            else:
                output_path = None
            try:
                process_file(filepath, output_path, mode)
                print(f"处理完成: {filepath} ({'正向' if mode == 'forward' else '反向'})")
            except Exception as e:
                print(f"处理文件 {filepath} 时出错: {e}")

def main():
    parser = argparse.ArgumentParser(description='二进制文件处理工具')
    parser.add_argument('input', help='输入目录路径')
    parser.add_argument('-o', '--output', help='输出目录路径（可选）')
    
    # 使用互斥组确保-d和-r不能同时使用
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--forward', action='store_true', 
                      help='正向处理模式（00->0D0A，0101->#endline）')
    group.add_argument('-r', '--reverse', action='store_true', 
                      help='反向处理模式（0D0A->00，#endline->0101，包括后面的0D0A）')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.input):
        print(f"错误: {args.input} 不是有效的目录")
        sys.exit(1)
    
    # 确定处理模式（默认正向）
    mode = 'reverse' if args.reverse else 'forward'
    
    process_directory(args.input, args.output, mode)

if __name__ == '__main__':
    main()