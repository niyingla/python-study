"""
# 定义空字符串
info = ''
info2 = str() # 类实例化定义
print(info)
print(info2)
print(type(info))
print(type(info2))
# 定义非空字符串
info3 = '不是空字符串'
info4 = "不是空字符串"
# info5 = "不是空字符串"
print(type(info3))
print(type(info4))
print(type(info5))
"""
# 字符串的特殊处理
# data = 'I\'m tom'
# find查找
info = '黑马程序员'
info.find('黑')
print(info.find('黑'))
# replace 替换
info2 = '盒马程序员'
info3 = info.replace('盒', '黑')
print(info3)
# 分割 split
info4 = 'hello world and si and int'
info6 = info4.split('and')
print(info4.split())
print(info6)
# 链接 join
num = ['python', 'java', 'php']
print(' and '.join(num))
num2 = ['黑马', '白马', '野马']
print(' 是 '.join(num2))
