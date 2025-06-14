import os
import re
from tkinter import Tk, filedialog

# 打开文件选择对话框，选择一个文件
root = Tk()
root.withdraw()  # 不显示主窗口
file_path = filedialog.askopenfilename(title="选择一个文件", filetypes=[("Java Files", "*.java")])

if file_path:
    # 输入 A 和 B
    A = int(input("请输入起始行 : "))
    B = input("请输入叠加行数 (默认 1): ")

    # 如果 B 为空，则默认值为 1
    B = int(B) if B else 1

    # 正则表达式匹配 sort = 数字
    pattern = re.compile(r'sort\s*=\s*(\d+)')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 替换所有的 sort = 数字
    def replace(match):
        sort_value = int(match.group(1))
        if sort_value >= A:
            return f'sort = {sort_value + B}'
        return match.group(0)

    # 替换匹配到的部分
    updated_content = re.sub(pattern, replace, content)

    # 将修改后的内容写回原文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("文件已更新。")
else:
    print("未选择文件。")