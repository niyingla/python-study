# 导包
import json

# 找到文件
test_data = 'data/tata1.json'
# 写入的数据
param = {'name': '张三', 'age': 16}
# 打开文件
with open('test_data', 'w', encoding='utf-8') as f:
    # 操作文件:写入
    json.dump(param, f, ensure_ascii=False)
# 自动关闭文件
