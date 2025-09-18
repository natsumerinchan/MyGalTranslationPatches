import json
import re

def adjust_text(orig_text, trans_text):
    """
    调整翻译文本：
    1. 保持开头和结尾的特殊字符位置不变
    2. 确保\r\n位置与原始文本完全一致
    3. 计算需要添加的全角空格数量
    """
    # 检查原始文本的开头和结尾特殊字符
    orig_start_pattern = r'^([「　（]+)'
    orig_end_pattern = r'([」）]+)$'
    
    orig_start_match = re.search(orig_start_pattern, orig_text)
    orig_end_match = re.search(orig_end_pattern, orig_text)
    
    orig_start_chars = orig_start_match.group(1) if orig_start_match else ""
    orig_end_chars = orig_end_match.group(1) if orig_end_match else ""
    
    # 移除开头和结尾特殊字符，获取中间内容
    orig_middle = orig_text[len(orig_start_chars):]
    if orig_end_chars:
        orig_middle = orig_middle[:-len(orig_end_chars)]
    
    # 对翻译文本进行相同的处理
    trans_start_match = re.search(orig_start_pattern, trans_text)
    trans_end_match = re.search(orig_end_pattern, trans_text)
    
    trans_start_chars = trans_start_match.group(1) if trans_start_match else orig_start_chars
    trans_end_chars = trans_end_match.group(1) if trans_end_match else orig_end_chars
    
    # 移除翻译文本的开头和结尾特殊字符
    trans_middle = trans_text[len(trans_start_chars):]
    if trans_end_chars:
        trans_middle = trans_middle[:-len(trans_end_chars)]
    
    # 移除翻译文本中的所有换行符，只保留纯文本内容
    trans_clean = re.sub(r'[\r\n]', '', trans_middle)
    
    # 按照原始文本中间内容的换行符位置重新构建翻译文本
    result_middle = ""
    trans_index = 0
    trans_length = len(trans_clean)
    
    # 遍历原始文本中间内容的每个字符
    for char in orig_middle:
        if char in ['\r', '\n']:
            # 保持原始文本的换行符位置
            result_middle += char
        elif trans_index < trans_length:
            # 添加翻译文本的字符
            result_middle += trans_clean[trans_index]
            trans_index += 1
        else:
            # 翻译文本长度不足，用全角空格填充
            result_middle += '\u3000'
    
    # 如果翻译文本还有剩余字符，添加到末尾
    if trans_index < trans_length:
        result_middle += trans_clean[trans_index:]
    
    # 重新组合完整的文本
    result = trans_start_chars + result_middle + trans_end_chars
    
    return result

def process_json_files(orig_file, trans_file):
    """处理两个JSON文件"""
    try:
        # 读取原始JSON文件
        with open(orig_file, 'r', encoding='utf-8') as f:
            orig_data = json.load(f)
        
        # 读取翻译JSON文件
        with open(trans_file, 'r', encoding='utf-8') as f:
            trans_data = json.load(f)
        
        # 确保两个JSON都是数组格式
        if not isinstance(orig_data, list) or not isinstance(trans_data, list):
            print("错误：JSON文件必须是数组格式")
            return False
        
        if len(orig_data) != len(trans_data):
            print("警告：两个JSON数组长度不一致")
        
        # 遍历数组中的每个对象
        modified = False
        for i, (orig_obj, trans_obj) in enumerate(zip(orig_data, trans_data)):
            # 确保都是字典对象
            if not isinstance(orig_obj, dict) or not isinstance(trans_obj, dict):
                continue
            
            # 只处理包含message键的对象
            if 'message' in orig_obj and 'message' in trans_obj:
                orig_message = orig_obj['message']
                trans_message = trans_obj['message']
                
                # 只处理字符串类型的message
                if isinstance(orig_message, str) and isinstance(trans_message, str):
                    # 检查是否需要特殊处理（包含特殊开头或结尾）
                    has_special_start = re.match(r'^[「　（]', orig_message)
                    has_special_end = re.search(r'[」）]$', orig_message)
                    
                    if has_special_start or has_special_end:
                        # 调整文本（保持特殊字符位置和换行符）
                        adjusted_text = adjust_text(orig_message, trans_message)
                        if adjusted_text != trans_message:
                            trans_obj['message'] = adjusted_text
                            modified = True
                            print(f"已调整第{i+1}个对象的message（特殊字符处理）")
                    else:
                        # 普通文本处理 - 确保换行符位置完全一致
                        trans_clean = re.sub(r'[\r\n]', '', trans_message)
                        result = ""
                        trans_index = 0
                        trans_length = len(trans_clean)
                        
                        # 按照原始文本的换行符位置重新构建
                        for char in orig_message:
                            if char in ['\r', '\n']:
                                # 保持原始文本的换行符
                                result += char
                            elif trans_index < trans_length:
                                # 添加翻译文本的字符
                                result += trans_clean[trans_index]
                                trans_index += 1
                            else:
                                # 翻译文本长度不足，用全角空格填充
                                result += '\u3000'
                        
                        # 如果翻译文本还有剩余字符，添加到末尾
                        if trans_index < trans_length:
                            result += trans_clean[trans_index:]
                        
                        if result != trans_message:
                            trans_obj['message'] = result
                            modified = True
                            print(f"已调整第{i+1}个对象的message")
        
        # 如果有修改，保存回文件
        if modified:
            with open(trans_file, 'w', encoding='utf-8') as f:
                json.dump(trans_data, f, ensure_ascii=False, indent=2)
            print(f"已更新文件: {trans_file}")
        else:
            print("无需修改")
        
        return True
        
    except Exception as e:
        print(f"处理文件时出错: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    orig_file = "orig/TBLSTR.json"
    trans_file = "trans/TBLSTR.json"
    
    print("开始处理JSON文件...")
    print(f"原始文件: {orig_file}")
    print(f"翻译文件: {trans_file}")
    
    success = process_json_files(orig_file, trans_file)
    
    if success:
        print("处理完成！")
    else:
        print("处理失败！")