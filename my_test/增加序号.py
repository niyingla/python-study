import os
import re

# 输入 A 和 B
A = int(input("请输入起始累加序号 : "))
B = input("请输入默认累计序号 (默认 1): ")

# 如果 B 为空，则默认值为 1
B = int(B) if B else 1

# 获取当前目录下的所有 .java 文件
java_files = [f for f in os.listdir('.') if f.endswith('.java')]

# 正则表达式匹配 sort = 数字
pattern = re.compile(r'sort\s*=\s*(\d+)')

for java_file in java_files:
    with open(java_file, 'r', encoding='utf-8') as file:
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
    with open(java_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)