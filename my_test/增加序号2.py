import re
from tkinter import Tk, filedialog, Text, Scrollbar, Button, Label, Entry

# 创建 Tkinter 窗口
root = Tk()
root.title("文件修改工具")

# 创建标签和输入框
Label(root, text="请输入起始行数值:").pack()
entry_A = Entry(root)
entry_A.pack()

Label(root, text="请输入叠加行数(默认 1):").pack()
entry_B = Entry(root)
entry_B.pack()


# 默认 B 为 1，如果输入为空则使用默认值
def on_submit():
    A = int(entry_A.get()) if entry_A.get() else 0
    B = int(entry_B.get()) if entry_B.get() else 1

    # 打开文件选择对话框，选择一个文件
    file_path = filedialog.askopenfilename(title="选择一个文件", filetypes=[("Java Files", "*.java")])

    # 创建文本框显示修改内容
    text_box.delete(1.0, "end")  # 清空之前的内容
    text_box.insert("end", "修改内容:\n")

    if file_path:
        # 正则表达式匹配 sort = 数字
        pattern = re.compile(r'sort\s*=\s*(\d+)')

        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            # 查找并替换匹配到的 sort = 数字
            def replace(match):
                sort_value = int(match.group(1))
                if sort_value >= A :  # 判断 A 是否小于等于匹配到的数字
                    new_value = sort_value + B
                    updated_line = f"修改前: {match.group(0)} -> 修改后: sort = {new_value}\n"
                    text_box.insert("end", updated_line)  # 在窗口显示修改前后的内容
                    return f'sort = {new_value}'
                return match.group(0)

            updated_line = re.sub(pattern, replace, line)
            updated_lines.append(updated_line)

        # 将修改后的内容写回原文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(updated_lines)

        text_box.insert("end", "\n文件已更新。")
    else:
        text_box.insert("end", "未选择文件。")


# 创建滚动文本框显示修改后的内容
text_box = Text(root, height=15, width=80)
scrollbar = Scrollbar(root, command=text_box.yview)
text_box.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
text_box.pack()

# 创建提交按钮
submit_button = Button(root, text="提交", command=on_submit)
submit_button.pack()

# 启动 Tkinter 窗口
root.mainloop()