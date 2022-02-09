# try:
#     num = float(input('请输入一个数字:'))
# except ValueError:
#     print('输入的不是数字')
# else:
#     if num % 2 == 0:
#         print('偶数')
#     else:
#         print('基数')
#
num = input('请输入一串字符串:')
if num.isdigit():
    with open('a.txt', 'w', encoding='utf-8') as f:
        f.write(num)
else:
    print('提示输入内容有误')
# with open('b.txt',encoding='utf=8') as f:
#     info = f.read()
#     print(info)
#     print(info.split(','))
#     for i in info:
    #     print(i)
import json

param = {"name": "小明", "age": 18, 'sex': '男', 'hobby': ['听歌', '游戏', '购物', '吃饭', '睡觉', '打豆豆'],
         'address': {'country': '中国',
                     'city': '北京', 'street': '王府街'}}
with open('data.json', 'w', encoding="utf-8") as f:
    json.dump(param, f, ensure_ascii=False)
with open('data.json', encoding='utf-8') as f:
    info = json.load(f)
    print(info)
    print(info['name'])
    print(info['hobby'])
# import json
#
# with open('tpshop.json', encoding='utf-8') as f:
#     info = json.load(f)
#     print(info)
# print(info['msg'])
