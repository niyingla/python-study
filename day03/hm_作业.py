#  字符串的应用方法
#  字符查找 find :查找'程'的下标,并打印出来
info = '黑马程序员'
print(info.find('程'))
#  字符串的替换 replace :把'唱歌'替换成'跳舞',并打印出来
info1 = '小明喜欢唱歌'
print(info1.replace('唱歌', '跳舞'))
#  字符串的拆分 split : 把'and'拆分拼,并打印出来
info2 = 'Hello python and c++ and java'
print(info2.split('and'))
# 字符串链接 join 用'and'链接,并打印出来
info4 = ['python', 'c++', 'java', 'PHP']
print(' and '.join(info4))
# 列表的应用方法
# 列表的元素查询: 索引 查询李四,并打印出来
data = ['张三', '李四']
print(data[1])
# 列表的统计: 元素统计 count 统计Python出现的次数,并打印出来
data1 = ['python', 'c++', 'java', 'python']
print(data1.count('python'))
# 列表的增加: 末尾增加元素 append :在末尾添加元素'php',
data1.append('php')
print(data1)
# 列表的指定位置增加 :insert : 添加元素第二个位置,加个'php',并打印出来
data1.insert(1, 'php')
print(data1)
# 列表合并 extend 把data2和data3合并,并打印出来
data2 = [1, 2, 3]
data3 = [4, 5, 6, 7]
data2.extend(data3)
print(data2)
# 列表元素的删除:指定索引位置删除pop  : 把data1的第一个'php'删除,并打印出来
data1.pop(1)
print(data1)
# 列表指定元素删除 remove : 把data1的第一个'python'删除,并打印出来
data1.remove('python')
print(data1)
# 列表元素的修改: 修改指定索引的数据 :把data1的'c++'修改成''c++语言,并打印出来
data1[0] = 'c++语言'
print(data1)
# 列表的反转 : 元素倒置 reverse 把data2到置并打印出来
data2.reverse()
print(data2)
# 列表元素的大小排序 data2从大到小排序,并打印出来
data2.sort(reverse=True)
print(data2)
# data2从小到大排序,并打印出来
data2.sort(reverse=False)
print(data2)
# 嵌套的列表用下标查询元素 查询'王五',并打印出来
data4 = [['张三','李四'],[33,55,['功能测试','王五']]]
print(data4[1][2][1])
# 元组的应用方法
# 元组的查询: 索引  查询num下标为2的对应元素 并打印出来
num = ('张三',22,1.78)
print(num[2])
# 元组的统计 count 统计num'22'出现的次数,并打印出来
print(num.count(22))
# 字典的应用方法
# 字典的新增与修改值
num1 = {'name':'张三'}
num1['name'] = '李四' #  修改
print(num1)
num1['age'] = 18   # 新增
print(num1)
# 字典的删除值 pop num1删除年龄18 ,并打印出来
num1.pop('age')
print(num1)