# 定义空列表
info = []
info1 = list()  # 类实例化
print(info)
print(info1)
# 定义不是空列表
info2 = ['张三', '李四']
# list的查询方法 索引
data = ['张三', '李四']
data1 = data[0]
print(data1)
print(data)
# count 查询元素出现的次数
data2 = ['python', 'c++', 'python', 'java']
print(data2.count('python'))
print(data2.count('java'))
# append 增加末尾一条数据
"""
data3 = ['web自动化','UI自动化','接口自动化']
data3.append('app自动化')
print(data3)
data3.append("12")
print(data3)
data3.append(12.34)
print(data3)
"""
# 指定位置追加 insert
"""
data4 = ['web自动化', 'UI自动化', '接口自动化']
data4.insert(1, 'app自动化')
print(data4)
data4.insert(6, '数字化')  # 没有下标直接添加到末尾
print(data4)
# 列表的删除指定位置的删除 pop
data4.pop(2)
print(data4)
data4.pop(0)
print(data4)
# 列表删除指定的元素 remove
data4.remove('app自动化')
print(data4)
data4.remove('数字化')
print(data4)
"""
# 列表的修改 索引
data5 = ['web自动化', 'UI自动化', '接口自动化', 'app自动化']
data5[1] = '性能自动化'
print(data5)
# 列表翻转 reverse
data6 = [3, 6, 78, 9, 2, 4, 5, 6, ]
data6.reverse()
print(data6)
# 列表的排序 sort
data6.sort(reverse=False)  # 从小到大
print(data6)
data6.sort(reverse=True)  # 从大到小
print(data6)
# 列表的嵌套
# 获取指定的元素
data7 = [['web自动化', 'UI自动化', ['接口自动化','哈哈'], 'app自动化'], [3, 6, 78, 9, 2, 4, 5, 6, ]]
print(data7[1][1])
print(data7[0][2][1])