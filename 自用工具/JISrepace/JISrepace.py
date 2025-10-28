import json
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os
import sys

class CharReplacerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简中日繁转换工具")
        self.root.geometry("650x500")
        
        # 初始化替换表
        self.substitution_table = {}
        self.reverse_table = {}
        self.duplicate_warnings = []
        self.non_encodable_warnings = []
        
        # 当前选择的编码
        self.encoding = "CP932"
        self.encodings = {
            "CP932": "cp932",
            "Shift_JIS": "shift_jis"
        }
        
        # 创建UI元素
        self.create_widgets()
        
        # 尝试加载默认的替换表
        default_path = "subs_cn_jp.json"
        if os.path.exists(default_path):
            self.load_substitution_table(default_path)
        else:
            messagebox.showinfo("提示", "请先加载替换表文件 (subs_cn_jp.json)")
    
    def create_widgets(self):
        # 顶部菜单
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="加载替换表", command=self.load_table_dialog)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="文件", menu=filemenu)
        self.root.config(menu=menubar)
        
        # 控制面板框架
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        # 编码选择
        encoding_label = tk.Label(control_frame, text="目标编码:")
        encoding_label.pack(side="left", padx=5)
        
        self.encoding_var = tk.StringVar(value=self.encoding)
        self.encoding_menu = ttk.Combobox(
            control_frame,
            textvariable=self.encoding_var,
            values=list(self.encodings.keys()),
            state="readonly",
            width=10
        )
        self.encoding_menu.pack(side="left", padx=5)
        self.encoding_menu.bind("<<ComboboxSelected>>", self.change_encoding)
        
        # 替换表信息显示
        self.table_info_label = tk.Label(control_frame, text="未加载替换表", anchor="w")
        self.table_info_label.pack(side="left", padx=10, expand=True, fill="x")
        
        # 输入输出框架
        io_frame = tk.Frame(self.root)
        io_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # 输入文本框
        input_label = tk.Label(io_frame, text="输入文本:")
        input_label.pack(anchor="w")
        self.input_text = tk.Text(io_frame, height=8, wrap="word")
        self.input_text.pack(fill="both", expand=True)
        
        # 按钮框架
        button_frame = tk.Frame(io_frame)
        button_frame.pack(fill="x", pady=5)
        
        replace_button = tk.Button(
            button_frame, 
            text="正向替换(简中→日繁)", 
            command=lambda: self.replace_chars(forward=True)
        )
        replace_button.pack(side="left", padx=5)
        
        reverse_button = tk.Button(
            button_frame, 
            text="反向替换(日繁→简中)", 
            command=lambda: self.replace_chars(forward=False)
        )
        reverse_button.pack(side="left", padx=5)
        
        clear_button = tk.Button(button_frame, text="清空", command=self.clear_text)
        clear_button.pack(side="left", padx=5)
        
        # 替换方向说明标签
        direction_label = tk.Label(
            button_frame, 
            text="正向:左→右 反向:左←右", 
            fg="gray"
        )
        direction_label.pack(side="right", padx=5)
        
        # 输出文本框
        output_label = tk.Label(io_frame, text="输出文本:")
        output_label.pack(anchor="w")
        self.output_text = tk.Text(io_frame, height=8, wrap="word")
        self.output_text.pack(fill="both", expand=True)
        
        # 警告信息显示
        self.warning_label = tk.Label(self.root, text="", fg="red", anchor="w")
        self.warning_label.pack(fill="x", padx=10, pady=5)
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(
            self.root, 
            textvariable=self.status_var,
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W
        )
        self.status_bar.pack(fill="x")
        self.update_status(f"当前编码: {self.encoding}")
    
    def update_status(self, message):
        self.status_var.set(message)
    
    def change_encoding(self, event=None):
        self.encoding = self.encoding_var.get()
        self.update_status(f"当前编码: {self.encoding}")
        if self.substitution_table:
            messagebox.showinfo(
                "编码已更改", 
                f"编码已切换为 {self.encoding}，请重新加载替换表以应用新编码"
            )
    
    def is_encodable(self, char):
        """检查字符是否可以用当前编码表示"""
        try:
            char.encode(self.encodings[self.encoding])
            return True
        except UnicodeEncodeError:
            return False
    
    def load_table_dialog(self):
        file_path = filedialog.askopenfilename(
            title="选择替换表文件",
            filetypes=[("JSON文件", "*.json"), ("所有文件", "*.*")]
        )
        if file_path:
            self.load_substitution_table(file_path)
    
    def load_substitution_table(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self.substitution_table = {}
            self.reverse_table = {}
            self.duplicate_warnings = []
            self.non_encodable_warnings = []
            
            # 检查替换表中的问题并构建正向和反向表
            for target, replacement in data.items():
                if len(target) != 1 or len(replacement) != 1:
                    self.non_encodable_warnings.append(f"忽略非单字符替换项: '{target}' -> '{replacement}'")
                    continue
                
                if target == replacement:
                    self.duplicate_warnings.append(f"目标与替换字符相同: '{target}'")
                    continue
                
                # 正向替换表：替换字符必须是目标编码
                if not self.is_encodable(replacement):
                    self.non_encodable_warnings.append(
                        f"替换字符 '{replacement}' 不是{self.encoding}字符"
                    )
                    continue
                
                # 添加到正向替换表
                self.substitution_table[target] = replacement
                
                # 添加到反向替换表（无条件添加，不检查编码）
                self.reverse_table[replacement] = target
            
            # 更新UI显示
            self.table_info_label.config(
                text=f"已加载替换表: {os.path.basename(file_path)}\n"
                     f"正向替换项: {len(self.substitution_table)} "
                     f"反向替换项: {len(self.reverse_table)} "
                     f"(编码: {self.encoding})"
            )
            
            # 显示警告
            warnings = []
            if self.duplicate_warnings:
                warnings.append(f"{len(self.duplicate_warnings)} 个目标与替换字符相同的项")
            if self.non_encodable_warnings:
                warnings.append(f"{len(self.non_encodable_warnings)} 个非{self.encoding}字符或其他问题")
            
            if warnings:
                self.warning_label.config(text="警告: " + "; ".join(warnings))
            else:
                self.warning_label.config(text="")
            
            # 显示详细警告
            if self.duplicate_warnings or self.non_encodable_warnings:
                detailed_warnings = self.duplicate_warnings + self.non_encodable_warnings
                messagebox.showwarning(
                    "替换表警告",
                    "替换表中发现以下问题:\n\n" + "\n".join(detailed_warnings[:10]) + 
                    ("\n\n(只显示前10条警告)" if len(detailed_warnings) > 10 else "")
                )
        
        except Exception as e:
            messagebox.showerror("错误", f"加载替换表失败: {str(e)}")
    
    def replace_chars(self, forward=True):
        if not self.substitution_table:
            messagebox.showwarning("警告", "请先加载有效的替换表")
            return
        
        input_text = self.input_text.get("1.0", "end-1c")
        if not input_text.strip():
            messagebox.showwarning("警告", "请输入要替换的文本")
            return
        
        output_text = []
        missing_replacements = set()
        
        # 根据方向选择使用哪个替换表
        table = self.substitution_table if forward else self.reverse_table
        direction_desc = "正向" if forward else "反向"
        
        for char in input_text:
            if forward:
                # 正向替换逻辑：非目标编码字符才替换
                if self.is_encodable(char):
                    output_text.append(char)
                else:
                    if char in table:
                        output_text.append(table[char])
                    else:
                        output_text.append(char)
                        missing_replacements.add(char)
            else:
                # 反向替换逻辑：直接查找替换表，不考虑编码
                if char in table:
                    output_text.append(table[char])
                else:
                    output_text.append(char)
        
        # 显示结果
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", "".join(output_text))
        
        # 显示缺失替换的警告（仅正向替换）
        if missing_replacements and forward:
            missing_chars = ", ".join(f"'{c}'" for c in sorted(missing_replacements))
            messagebox.showwarning(
                "替换警告",
                f"以下非{self.encoding}字符在{direction_desc}替换表中没有对应的替换字符:\n{missing_chars}"
            )
    
    def clear_text(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharReplacerApp(root)
    root.mainloop()