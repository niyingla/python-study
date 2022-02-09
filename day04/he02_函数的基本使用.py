# 定义打招呼的函数
def say_hello():
    """函数注释"""
    print('hello')
    print('hello')
    print('hello')


say_hello()


# 定义函数
def sum_2_sum(num, num1):
    """两个数字求和"""
    result = num + num1
    print(result)
    return result  # 返回值的函数
    print('看看我执行不')


# 调用函数
print(sum_2_sum(10, 20))


# 比较参数
def get_max(data, data1):
    if data > data1:
        return data
    else:
        return data1


print(get_max(1, 3))


# 函数的嵌套调用
def test1():
    print('第一个函数')


def test2():
    print('第二个函数')
    test1()


test2()
