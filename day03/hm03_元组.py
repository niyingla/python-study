# 元组空的定义
info = ()
info1 = tuple()  # 类实例化定义
print(info)
print(info1)
# 元组非空的定义
info2 = (0, 1, 2, 3)
print(info2)
info3 = 1, 2, 3, 4
print(info3)
# 结论:元组的括号可省略
#  元组只有一个元素时,加括号并且后面加逗号
# 元组元素查询 索引
info4 = (11, 'bbb', 2.22)
print(info4[2])
#  查询统计的数量 count
info5 = (0, 1, 2, 3, 2)
print(info5.count(2))
# 笔试题 数据交换
num = 100
num1 = 200
num, num1 = num1, num
print(f'num:{num},num1:{num1}')
