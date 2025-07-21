import argparse
import os
import glob
import sys


def diss(script_mes: str, file_txt: str, version: int = 1, encoding: str = 'cp932'):
    from ai6win_mes import AI6WINScript

    new_script = AI6WINScript(script_mes, file_txt, encoding=encoding, verbose=True, debug=False, version=version)
    new_script.disassemble()
    del new_script


def ass(script_mes: str, file_txt: str, version: int = 1, encoding: str = 'cp932'):
    from ai6win_mes import AI6WINScript

    new_script = AI6WINScript(script_mes, file_txt, encoding=encoding, verbose=True, debug=False, version=version)
    new_script.assemble()
    del new_script


def batch_diss(mes_dir: str, txt_dir: str, version: int = 1, encoding: str = 'cp932'):
    """批量反编译目录中的所有.mes文件"""
    mes_dir = os.path.abspath(mes_dir)
    txt_dir = os.path.abspath(txt_dir)
    
    if not os.path.exists(mes_dir):
        print(f"错误: mes目录不存在: {mes_dir}")
        return
    
    os.makedirs(txt_dir, exist_ok=True)
    
    mes_files = glob.glob(os.path.join(mes_dir, "*.mes"))
    if not mes_files:
        print(f"警告: 在 {mes_dir} 中未找到.mes文件")
        return
    
    print(f"开始批量反编译，找到 {len(mes_files)} 个文件...")
    
    for mes_file in mes_files:
        base_name = os.path.splitext(os.path.basename(mes_file))[0]
        txt_file = os.path.join(txt_dir, f"{base_name}.txt")
        
        try:
            print(f"反编译: {os.path.basename(mes_file)} -> {os.path.basename(txt_file)}")
            diss(mes_file, txt_file, version, encoding)
            print(f"成功: {os.path.basename(txt_file)}")
        except Exception as e:
            print(f"失败: {os.path.basename(mes_file)} - {str(e)}")


def batch_ass(mes_dir: str, txt_dir: str, version: int = 1, encoding: str = 'cp932'):
    """批量编译目录中的所有.txt文件"""
    mes_dir = os.path.abspath(mes_dir)
    txt_dir = os.path.abspath(txt_dir)
    
    if not os.path.exists(txt_dir):
        print(f"错误: txt目录不存在: {txt_dir}")
        return
    
    os.makedirs(mes_dir, exist_ok=True)
    
    txt_files = glob.glob(os.path.join(txt_dir, "*.txt"))
    if not txt_files:
        print(f"警告: 在 {txt_dir} 中未找到.txt文件")
        return
    
    print(f"开始批量编译，找到 {len(txt_files)} 个文件...")
    
    for txt_file in txt_files:
        base_name = os.path.splitext(os.path.basename(txt_file))[0]
        mes_file = os.path.join(mes_dir, f"{base_name}.mes")
        
        try:
            print(f"编译: {os.path.basename(txt_file)} -> {os.path.basename(mes_file)}")
            ass(mes_file, txt_file, version, encoding)
            print(f"成功: {os.path.basename(mes_file)}")
        except Exception as e:
            print(f"失败: {os.path.basename(txt_file)} - {str(e)}")


parser = argparse.ArgumentParser(prog="AI6WINScriptTool", description="Assembler and disassembler of AI6WIN engine scripts")
subparsers = parser.add_subparsers(dest='mode', help="处理模式")

# 单文件模式
single_parser = subparsers.add_parser('single', help="单文件模式")
single_parser.add_argument('action', choices=["d", "a"], help="操作类型: d=反编译, a=编译")
single_parser.add_argument('mes_file', help="Mes文件路径")
single_parser.add_argument('txt_file', help="Txt文件路径")
single_parser.add_argument('-v', '--version', dest="version",
                          choices=[0, 1], default=1, required=False, type=int, help="Mes版本")
single_parser.add_argument('-e', '--encoding', dest="encoding", default='cp932', required=False, help="字符串编码")

# 批量模式
batch_parser = subparsers.add_parser('batch', help="批量处理模式")
batch_parser.add_argument('action', choices=["d", "a"], help="操作类型: d=反编译, a=编译")
batch_parser.add_argument('mes_dir', help="Mes文件目录")
batch_parser.add_argument('txt_dir', help="Txt文件目录")
batch_parser.add_argument('-v', '--version', dest="version",
                         choices=[0, 1], default=1, required=False, type=int, help="Mes版本")
batch_parser.add_argument('-e', '--encoding', dest="encoding", default='cp932', required=False, help="字符串编码")

# 为了保持向后兼容，支持旧的调用方式
if len(sys.argv) > 1 and sys.argv[1] not in ['single', 'batch']:
    # 旧版兼容模式
    parser = argparse.ArgumentParser(prog="AI6WINScriptTool", description="Assembler and disassembler of AI6WIN engine scripts")
    parser.add_argument('action', choices=["d", "a"], help="Action")  # disassemble, assemble.
    parser.add_argument('mes_file', help="Mes file")
    parser.add_argument('txt_file', help="Txt file")
    parser.add_argument('-v', '--version', dest="version",
                        choices=[0, 1], default=1, required=False, type=int, help="Mes version")
    parser.add_argument('-e', '--encoding', dest="encoding", default='cp932', required=False, help="Strings encoding")

    argdata = parser.parse_args()
    action = argdata.action
    mes_file = argdata.mes_file
    txt_file = argdata.txt_file
    version = argdata.version
    encoding = argdata.encoding
    if action == 'd':
        diss(mes_file, txt_file, version, encoding)
    else:
        ass(mes_file, txt_file, version, encoding)
else:
    # 新版参数解析
    argdata = parser.parse_args()
    if argdata.mode == 'single':
        if argdata.action == 'd':
            diss(argdata.mes_file, argdata.txt_file, argdata.version, argdata.encoding)
        else:
            ass(argdata.mes_file, argdata.txt_file, argdata.version, argdata.encoding)
    elif argdata.mode == 'batch':
        if argdata.action == 'd':
            batch_diss(argdata.mes_dir, argdata.txt_dir, argdata.version, argdata.encoding)
        else:
            batch_ass(argdata.mes_dir, argdata.txt_dir, argdata.version, argdata.encoding)
    else:
        parser.print_help()
