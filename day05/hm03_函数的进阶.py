# 缺省参数的应用
def per_info(name, title='', gender='男'):
    """

    :param name: 姓名
    :param title: 职位
    :param gender: 年龄
    :return:
    """
    print(f'姓名:{name},职位:{title},年龄:{gender}')


per_info('李四', '班长')
per_info('李四', '班长', '女')


# 结论 定义缺省参数的函数是,缺省参数必须放到普通函数的后面

# 多值参数
def demo(*args):
    """

    :param args: 多个参数
    :return:
    """
    print(args)


demo(1)


# 结论 传递进去的实参个数最终结果是元组类型的数据
# 例题
def sum_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result


num = (1, 2, 3, 4)  # 定义一个元组
print(sum_numbers(*num))  # 将整个元组作为实参,需要先拆包,再传递

# 匿名函数

result = lambda x, y: x + y
print(result(2, 1))
# 结论 有参数输入并且有返回值的基本计算,可以使用匿名函数(减少代码量)
# 案例
# user_list = [{'name': '张三', 'age': 22, 'title': '测试工程师'}, {'name': '李四', 'age': 24, 'title': '开发工程师'},
#              {'name': '王五', 'age': 21, 'title': '测试工程师'}]
# # 按照年排序:先把字典元素中的年龄取出来,然后才能排序
# # 通过匿名函数获取字典中年龄对应的值,然后排序
# value = lambda x: x['age']
# # x相当于每个字典元素
# # key 对应的值相当于一堆年龄的组合
# user_list.sort(key=value)
# print(user_list)
# user_list.sort(key=value, reverse=True)
# print(user_list)
user_list = [{'name': '张三', 'age': 22, 'title': '测试工程师'}, {'name': '李四', 'age': 24, 'title': '开发工程师'},
             {'name': '王五', 'age': 21, 'title': '测试工程师'}]
value = lambda x: x['age']
user_list.sort(key=value)
print(user_list)
user_list.sort(key=value, reverse=True)
print(user_list)
