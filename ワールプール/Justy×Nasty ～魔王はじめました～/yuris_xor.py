#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct
import argparse
import os
import sys

# 版本对应密钥配置
Keys = [
    {'min': 0x1E1, 'max': 0x1E8, 'key': b'\x0B\x8F\x00\xB1'},
    {'min': 0x0, 'max': 0x22A, 'key': b'\xD3\x6F\xAC\x96'},
    {'min': 0x22B, 'max': 0xFFF, 'key': b'\xA9\xF8\xCC\x66'},
]

def get_match_item(items, version):
    """根据版本号查找匹配项"""
    for item in items:
        if item['min'] <= version <= item['max']:
            return item
    return None

def xor_bytes(data, key):
    """使用密钥对数据进行异或操作"""
    if not key or len(key) == 0:
        return data
    key_len = len(key)
    return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])

def process_ybn_file(input_path, output_path, user_key=None):
    """处理YBN文件（加密/解密）"""
    with open(input_path, 'rb') as f:
        data = f.read()
    
    if len(data) < 8:
        print(f"错误：文件过小 ({len(data)} bytes)")
        return False
    
    # 读取版本号 (offset 4, 4 bytes little-endian)
    version = struct.unpack('<I', data[4:8])[0]
    print(f"文件版本: 0x{version:X}")
    
    # 确定文件结构类型
    if version >= 0x1C2:  # Type 1 结构
        header_len = 0x20
        cmd_len = struct.unpack('<I', data[0xC:0x10])[0]
        para_len = struct.unpack('<I', data[0x10:0x14])[0]
        str_len = struct.unpack('<I', data[0x14:0x18])[0]
        other_len = struct.unpack('<I', data[0x18:0x1C])[0]
        struct_type = 1
    else:  # Type 2 结构
        header_len = 0x20
        cmd_len = struct.unpack('<I', data[0x8:0xC])[0]
        para_len = 0
        str_len = struct.unpack('<I', data[0xC:0x10])[0]
        other_len = 0
        struct_type = 2
    
    # 计算各部分偏移量
    sections = {
        'header': (0, header_len),
        'cmd': (header_len, header_len + cmd_len),
        'para': (header_len + cmd_len, header_len + cmd_len + para_len),
        'str': (header_len + cmd_len + para_len, header_len + cmd_len + para_len + str_len),
        'other': (header_len + cmd_len + para_len + str_len, 
                 header_len + cmd_len + para_len + str_len + other_len)
    }
    
    # 分割文件内容
    file_parts = {}
    for name, (start, end) in sections.items():
        file_parts[name] = data[start:end]
    
    # 获取密钥
    if user_key:
        key = user_key
        print(f"使用自定义密钥: {key.hex().upper()}")
    else:
        key_item = get_match_item(Keys, version)
        if key_item:
            key = key_item['key']
            print(f"使用自动匹配密钥: {key.hex().upper()}")
        else:
            print(f"错误：找不到版本 0x{version:X} 对应的密钥")
            return False
    
    # 对加密部分进行异或操作
    for name in ['cmd', 'para', 'str', 'other']:
        if file_parts[name]:
            file_parts[name] = xor_bytes(file_parts[name], key)
    
    # 重新组合文件
    new_data = b''.join([
        file_parts['header'],
        file_parts['cmd'],
        file_parts['para'],
        file_parts['str'],
        file_parts['other']
    ])
    
    # 写入输出文件
    with open(output_path, 'wb') as f:
        f.write(new_data)
    
    print(f"成功处理文件: {output_path}")
    return True

def parse_key(key_str):
    """解析密钥字符串"""
    if key_str.startswith('0x'):
        try:
            return bytes.fromhex(key_str[2:])
        except ValueError:
            pass
    
    # 尝试解析\x格式
    if '\\x' in key_str:
        try:
            return key_str.encode('latin-1').decode('unicode_escape').encode('latin-1')
        except:
            pass
    
    # 尝试直接解析十六进制
    try:
        return bytes.fromhex(key_str)
    except ValueError:
        pass
    
    print(f"错误：无效的密钥格式 '{key_str}'")
    print("支持的格式: 十六进制字符串 (A9F8CC66) 或 转义格式 (\\xA9\\xF8\\xCC\\x66)")
    return None

def main():
    parser = argparse.ArgumentParser(description="Yu-ris引擎YBN脚本加解密工具")
    parser.add_argument("input", help="输入YBN文件路径")
    parser.add_argument("output", help="输出文件路径")
    parser.add_argument("-k", "--key", help="自定义密钥（十六进制或\\x??\\x??格式）")
    args = parser.parse_args()
    
    # 验证输入文件
    if not os.path.isfile(args.input):
        print(f"错误：输入文件不存在 '{args.input}'")
        sys.exit(1)
    
    # 解析密钥
    user_key = None
    if args.key:
        user_key = parse_key(args.key)
        if not user_key:
            sys.exit(1)
        if len(user_key) != 4:
            print("错误：密钥必须是4字节长度")
            sys.exit(1)
    
    # 处理文件
    success = process_ybn_file(args.input, args.output, user_key)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()