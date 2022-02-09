# 序列类型切片
# 按照指定要求获取一段数据
info = 'abcdefgh'
# adg
print(info[:8:3])
# 倒序
print(info[::-1])
# cde
print(info[2:5:1])
# 统计元素的个数 长度 len
info1 = ['数字',12,12.34]
print(len(info1))
print(type(len(info)))
# 清空字典和列表 针对可变的数据类型
# info1.clear()
print(info1)
# 拷贝字典和列表 针对可变的数据类型 copy
info2 = info1.copy()
print(info2)

