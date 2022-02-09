# 定义空字典
info = {}
info2 = dict()
print(info)
print(info2)
# 定义非空字典
info1 = {'name': '张三', 'age': 18}
print(type(info1))
# 结论 键名不能重复,键的数据类型可以任意,建议用字符串
# 字典元素的修改或增加
info3 = {'name': '张三'}
info3['name'] = '李四'  # 修改
print(info3)
info3['age'] = 18  # 增加
print(info3)
# 字典的删除 pop
info3.pop('age')
print(info3)
info3['age'] = 18
# 字典元素的查找 []
print(info3.get('name'))
print(info3['name'])
# 字典的查询方法 按键查值
info4 = {"name": "李四", "age": "18", "six": "男"}
print(info4['name'])
print(info4.get('name'))
print(info4.get('gender'))
# 字典数据的遍历
# 遍历字典的键
for i in info4.keys():
    print(i)
# 遍历字典的值
for i in info4.values():
    print(i)
# 遍历字典的键和值
for k, v in info4.items():
    print(f'{k}={v}')
# 练习题
# 1输入三组个人信息（分析每组信息数据类型）
# name = input('输入姓名：')
# age = int(input('输入年龄：'))
# six = input('输入性别：')
# 存入字典（定义一个非空的字典）
# per_info = {'name':name,'age':age,'gender':six}
# 定义空列表
var_list = []
# 循环三次完成添加
for i in range(3):
    name = input('输入姓名：')
    age = int(input('输入年龄：'))
    six = input('输入性别：')
    per_info = {'name': name, 'age': age, 'gender': six}
    var_list.append(per_info)
# 打印最后结果
print(var_list)
#  遍历列表
for i in var_list:
    print(i)
