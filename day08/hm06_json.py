# 直接读取JSON格式数据,结果为字典类型的数据
# 导包
import json
# 打开JSON文件
with open('data/data.json',encoding='utf-8') as f:
# 读取文件
    text = json.load(f)
    print(text)
# 自动关闭
# 结论:将JSON文件的数据直接转换为Python字典类型的数据
print(text['age'])
print(text['links'][0]['url'])
print(text['links'][1]['url'])
print(text['address']['street'])
print(text['numbers'])
for i in text['numbers']:
    print(i)
print(text['links'])
# 遍历links 取出TaoBao
for i in text['links']:
    if i.get('name') == 'TaoBao':
        print(i.get('name'))