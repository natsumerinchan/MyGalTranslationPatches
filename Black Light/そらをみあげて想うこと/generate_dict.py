import argparse

def generate_mapping_dict(input_text):
    lines = input_text.replace('\r', '').split('\n')  # 统一处理换行符
    mapping_dict = {}
    current_id = None
    
    for line in lines:
        line = line.strip()
        if line.startswith(':') and line[1:].isdigit():
            current_id = line[1:]  # 去掉冒号，保留数字部分
        elif current_id is not None:
            if line:  # 确保内容行不为空
                mapping_dict[current_id] = line
                current_id = None  # 重置current_id，以便处理下一个条目
    
    return mapping_dict

def format_mapping_output(mapping_dict):
    output_lines = []
    for key, value in sorted(mapping_dict.items()):
        output_lines.append(f"[@{key}]\t{value}")
    return output_lines

def process_file(input_file, output_file, input_encoding='cp932', output_encoding='cp932'):
    try:
        with open(input_file, 'r', encoding=input_encoding, newline='') as f:
            input_text = f.read()
        
        mapping_dict = generate_mapping_dict(input_text)
        output_lines = format_mapping_output(mapping_dict)
        
        with open(output_file, 'w', encoding=output_encoding, newline='\r\n') as f:
            f.write('\r\n'.join(output_lines))  # 显式使用\r\n换行
            
        return True
    except Exception as e:
        print(f"处理文件时出错: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='生成映射字典（默认使用cp932编码和Windows换行符）')
    parser.add_argument('-i', '--input', required=True, help='输入文件路径')
    parser.add_argument('-o', '--output', required=True, help='输出文件路径')
    parser.add_argument('--input-enc', default='cp932', help='输入文件编码（默认：cp932）')
    parser.add_argument('--output-enc', default='cp932', help='输出文件编码（默认：cp932）')
    
    args = parser.parse_args()
    
    if process_file(args.input, args.output, args.input_enc, args.output_enc):
        print(f"处理完成，结果已保存到 {args.output}（使用编码：{args.output_enc}，换行符：\\r\\n）")
    else:
        print("处理失败，请检查输入文件和编码设置")