def find_key(sample):
    sample_len = len(sample)
    key_len = 2
    key = sample[-key_len:]
    
    # 寻找可能的密钥长度
    while key_len * 2 < sample_len and sample[-key_len*2:-key_len] != key:
        key_len += 1
        key = sample[-key_len:]
    
    # 如果密钥长度超过样本长度的一半，返回 None
    if key_len * 2 >= sample_len:
        return None
    
    # 计算偏移量
    offset = key_len - sample_len % key_len
    
    # 生成密钥字符串
    key_string = "".join(chr((256 - key[(i + offset) % key_len]) % 256) for i in range(key_len))
    
    return key_string

if __name__ == "__main__":
    arc_file_path = input("Enter the *.arc file: ")
    
    try:
        with open(arc_file_path, "rb") as f:
            f.seek(8)  # 跳过前8个字节
            first_entry = f.read(32)  # 读取接下来的32个字节
        
        key = find_key(first_entry)
        
        if key:
            print(f"Guessed key: \"{key}\"")
        else:
            print("No key found.")
    
    except FileNotFoundError:
        print(f"File not found: {arc_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")