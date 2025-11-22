import xml.etree.ElementTree as ET
import json
import os
import argparse
from pathlib import Path
from typing import List, Dict, Any

class GameScriptProcessor:
    def __init__(self):
        self.text_resources = {}
    
    def extract_dialogue_from_xml(self, xml_file: str) -> List[Dict[str, str]]:
        """
        从XML文件中提取所有TextRes内容，包括被引用和未被引用的
        返回格式: [ {name, message} ] 或 [ {message} ]
        """
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # 解析TextResource部分
            text_resources = {}
            text_resource = root.find('TextResource')
            if text_resource is not None:
                for text_res in text_resource.findall('TextRes'):
                    no = text_res.get('NO')
                    text = text_res.text.strip() if text_res.text else ""
                    text_resources[no] = text
            
            dialogues = []
            used_text_resources = set()  # 记录已被Frame引用的文本资源
            
            # 首先处理被Frame引用的文本资源（保持原有逻辑）
            for frame in root.findall('Frame'):
                # 查找Log和Text元素
                log_elements = frame.findall('Log')
                text_elements = frame.findall('Text')
                
                # 处理每个Log元素（包含角色名和消息）
                for log in log_elements:
                    name_ref = log.get('NAME')
                    mess_ref = log.get('MESS')
                    
                    # 首先提取角色名（如果有的话）
                    if name_ref and name_ref != "-1" and name_ref in text_resources and name_ref not in used_text_resources:
                        name_text = text_resources[name_ref]
                        # 跳过内容为 ".xml" 的条目
                        if name_text != ".xml" and not name_text.endswith(".xml"):
                            dialogues.append({
                                "name": name_text,
                                "message": name_text
                            })
                        used_text_resources.add(name_ref)
                    
                    # 然后提取对话内容
                    if mess_ref and mess_ref in text_resources and mess_ref not in used_text_resources:
                        message = text_resources[mess_ref]
                        # 跳过内容为 ".xml" 的条目
                        if message != ".xml" and not message.endswith(".xml"):
                            # 构建对话对象
                            if name_ref and name_ref != "-1" and name_ref in text_resources:
                                dialogue_data = {
                                    "name": text_resources[name_ref],
                                    "message": message
                                }
                            else:
                                dialogue_data = {
                                    "message": message
                                }
                            
                            dialogues.append(dialogue_data)
                        used_text_resources.add(mess_ref)
                
                # 处理独立的Text元素（可能没有对应的Log）
                for text in text_elements:
                    mess_ref = text.get('MESS')
                    if mess_ref and mess_ref in text_resources and mess_ref not in used_text_resources:
                        message = text_resources[mess_ref]
                        # 跳过内容为 ".xml" 的条目
                        if message != ".xml" and not message.endswith(".xml"):
                            dialogues.append({
                                "message": message
                            })
                        used_text_resources.add(mess_ref)
            
            # 然后处理未被引用的TextRes节点
            for no, text in text_resources.items():
                if no not in used_text_resources:
                    # 跳过内容为 ".xml" 或以 ".xml" 结尾的条目
                    if text != ".xml" and not text.endswith(".xml"):
                        dialogues.append({
                            "message": text
                        })
            
            return dialogues
            
        except ET.ParseError as e:
            print(f"XML解析错误 {xml_file}: {e}")
            return []
        except Exception as e:
            print(f"处理文件 {xml_file} 时出错: {e}")
            return []
    
    def batch_extract(self, input_path: str, output_path: str):
        """
        批量提取XML到JSON，每个XML生成对应的JSON文件
        """
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        if input_path.is_file():
            # 单个文件处理
            dialogues = self.extract_dialogue_from_xml(str(input_path))
            
            # 确保输出目录存在
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(dialogues, f, ensure_ascii=False, indent=2)
            
            print(f"提取完成: {len(dialogues)} 条对话 -> {output_path}")
            
        elif input_path.is_dir():
            # 文件夹批量处理 - 每个XML生成对应的JSON
            if not output_path.exists():
                output_path.mkdir(parents=True, exist_ok=True)
            
            xml_files = list(input_path.glob("*.xml"))
            print(f"找到 {len(xml_files)} 个XML文件")
            
            total_dialogues = 0
            for xml_file in xml_files:
                print(f"处理文件: {xml_file.name}")
                dialogues = self.extract_dialogue_from_xml(str(xml_file))
                
                if dialogues:
                    # 生成对应的JSON文件名
                    json_filename = xml_file.stem + ".json"
                    json_path = output_path / json_filename
                    
                    # 保存为独立的JSON文件
                    with open(json_path, 'w', encoding='utf-8') as f:
                        json.dump(dialogues, f, ensure_ascii=False, indent=2)
                    
                    # 统计有name和无name的对话数量
                    with_name = sum(1 for d in dialogues if 'name' in d)
                    without_name = len(dialogues) - with_name
                    
                    print(f"  → 生成: {json_filename} ({len(dialogues)} 条对话, 有角色名: {with_name}, 无角色名: {without_name})")
                    total_dialogues += len(dialogues)
                else:
                    print(f"  → 警告: {xml_file.name} 没有提取到对话")
            
            print(f"批量提取完成: 共生成 {len(xml_files)} 个JSON文件，总计 {total_dialogues} 条对话 -> {output_path}")
        else:
            print(f"错误: 输入路径不存在 {input_path}")
    
    def repack_with_position_matching(self, original_xml_path: Path, original_json_path: Path, translated_json_path: Path, output_xml_path: Path):
        """
        使用位置一一对应匹配进行回封
        """
        try:
            # 读取原文JSON
            with open(original_json_path, 'r', encoding='utf-8') as f:
                original_dialogues = json.load(f)
            
            # 读取翻译JSON
            with open(translated_json_path, 'r', encoding='utf-8') as f:
                translated_dialogues = json.load(f)
            
            # 检查条目数量是否一致
            if len(original_dialogues) != len(translated_dialogues):
                print(f"错误: 条目数量不匹配！原文JSON有 {len(original_dialogues)} 条，翻译JSON有 {len(translated_dialogues)} 条")
                print("请确保翻译JSON与原文JSON的条目数量一致")
                return
            
            # 解析XML
            tree = ET.parse(original_xml_path)
            root = tree.getroot()
            
            # 获取XML中所有文本资源（按NO编号排序）
            text_resource = root.find('TextResource')
            if text_resource is None:
                print("错误: XML中没有找到TextResource")
                return
            
            # 获取所有TextRes节点并按NO编号排序
            text_res_nodes = list(text_resource.findall('TextRes'))
            text_res_nodes.sort(key=lambda x: int(x.get('NO', 0)))
            
            # 构建原文到NO的映射，跳过内容为".xml"的节点
            original_to_no = {}
            skipped_count = 0
            for text_res in text_res_nodes:
                original_text = text_res.text.strip() if text_res.text else ""
                # 跳过内容为 ".xml" 或以 ".xml" 结尾的节点
                if original_text == ".xml" or original_text.endswith(".xml"):
                    skipped_count += 1
                    continue
                original_to_no[original_text] = text_res.get('NO')
            
            if skipped_count > 0:
                print(f"跳过 {skipped_count} 个内容为 '.xml' 的文本节点")
            
            # 按位置一一对应更新，跳过内容为".xml"的条目
            updated_count = 0
            skipped_translations = 0
            
            for i in range(len(translated_dialogues)):
                original_message = original_dialogues[i].get('message', '')
                translated_message = translated_dialogues[i].get('message', '')
                
                # 跳过原文为".xml"或以".xml"结尾的条目
                if original_message == ".xml" or original_message.endswith(".xml"):
                    skipped_translations += 1
                    continue
                
                # 找到对应的XML节点
                if original_message in original_to_no:
                    target_no = original_to_no[original_message]
                    for text_res in text_res_nodes:
                        if text_res.get('NO') == target_no:
                            text_res.text = translated_message
                            updated_count += 1
                            break
            
            if skipped_translations > 0:
                print(f"跳过 {skipped_translations} 个内容为 '.xml' 的翻译条目")
            
            # 保存修改后的XML
            output_xml_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 添加XML声明和格式化
            tree_str = ET.tostring(root, encoding='utf-8').decode('utf-8')
            # 简单的格式化
            tree_str = tree_str.replace('><', '>\n<')
            
            with open(output_xml_path, 'w', encoding='utf-8') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
                f.write(tree_str)
            
            print(f"文件 {original_xml_path.name}: 更新了 {updated_count}/{len(translated_dialogues)} 条文本 -> {output_xml_path}")
            
        except Exception as e:
            print(f"回封文件 {original_xml_path} 时出错: {e}")
            import traceback
            traceback.print_exc()
    
    def batch_inject(self, input_xml_path: str, original_json_path: str, translated_json_path: str, output_xml_path: str):
        """
        批量将JSON翻译回封到XML，使用位置一一对应匹配
        """
        input_xml_path = Path(input_xml_path)
        original_json_path = Path(original_json_path)
        translated_json_path = Path(translated_json_path)
        output_xml_path = Path(output_xml_path)
        
        # 检查路径类型
        if (input_xml_path.is_dir() and 
            original_json_path.is_dir() and 
            translated_json_path.is_dir()):
            
            # 文件夹批量回封
            if not output_xml_path.exists():
                output_xml_path.mkdir(parents=True, exist_ok=True)
            
            xml_files = list(input_xml_path.glob("*.xml"))
            
            print(f"找到 {len(xml_files)} 个XML文件")
            
            processed_count = 0
            for xml_file in xml_files:
                # 查找对应的原文JSON和翻译JSON文件
                json_filename = xml_file.stem + ".json"
                original_json_file = original_json_path / json_filename
                translated_json_file = translated_json_path / json_filename
                
                if original_json_file.exists() and translated_json_file.exists():
                    try:
                        output_file = output_xml_path / xml_file.name
                        self.repack_with_position_matching(
                            xml_file, 
                            original_json_file, 
                            translated_json_file, 
                            output_file
                        )
                        processed_count += 1
                        
                    except Exception as e:
                        print(f"处理 {xml_file.name} 时出错: {e}")
                else:
                    missing_files = []
                    if not original_json_file.exists():
                        missing_files.append("原文JSON")
                    if not translated_json_file.exists():
                        missing_files.append("翻译JSON")
                    print(f"警告: 未找到 {json_filename} 的{', '.join(missing_files)}，跳过 {xml_file.name}")
            
            print(f"批量回封完成: 处理了 {processed_count} 个文件 -> {output_xml_path}")
        else:
            print("错误: 所有输入路径都必须是文件夹")
            print("请确保:")
            print("  - input_xmlORfolder: XML文件夹")
            print("  - original_jsonORfolder: 原文JSON文件夹") 
            print("  - translated_jsonORfolder: 翻译JSON文件夹")
            print("  - output_xmlORfolder: 输出XML文件夹")

def main():
    parser = argparse.ArgumentParser(description='游戏脚本XML-JSON转换工具')
    parser.add_argument('--dump', nargs=2, metavar=('input_xmlORfolder', 'output_jsonORfolder'), 
                       help='提取XML到JSON（每个XML生成对应的JSON）')
    parser.add_argument('--inject', nargs=4, metavar=('input_xmlORfolder', 'original_jsonORfolder', 'translated_jsonORfolder', 'output_xmlORfolder'), 
                       help='将JSON回封到XML（需要原文JSON和翻译JSON）')
    
    args = parser.parse_args()
    
    processor = GameScriptProcessor()
    
    if args.dump:
        input_path, output_path = args.dump
        processor.batch_extract(input_path, output_path)
        
    elif args.inject:
        input_xml, original_json, translated_json, output_xml = args.inject
        processor.batch_inject(input_xml, original_json, translated_json, output_xml)
        
    else:
        print("请使用 --dump 或 --inject 参数")
        print("示例:")
        print("  提取单个文件: python xmltool.py --dump script.xml dialogue.json")
        print("  提取整个文件夹: python xmltool.py --dump scripts/ json_output/")
        print("  回封: python xmltool.py --inject original_scripts/ original_jsons/ translated_jsons/ output_scripts/")

if __name__ == "__main__":
    main()