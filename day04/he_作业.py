"""
name = []
for i in range(5):
    name1 = input('请输入第一个名字:')
    name.append(name1)
print(name)
"""
"""
import random
name = []
for i in range(5):
    num = random.randint(0,len(name))
    name1 = input('请输入第一个名字:')
    name.append(name1)
print(name[num])
"""
"""
info = {"id": 10, "name": "周瑜", "age": 30}
info['sex'] = '男'
info['age'] = '25'
for v, w in info.items():
    print(f'键:{v}=值:{w}')
"""
"""
def my_func():
    for i in range(1,11):
        print('hello python')
    return i
my_func()
def my_test(num):
    if num % 2 != 0:
        return False
    else:
        return True
my_test(4)
"""
"""
def sum_test(n):
    result = 0
    for i in range(n+1):
        result = i+result
    print(result)
sum_test(6)
"""
"""
def triangle_test(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        if a==b==c:
            print('等边三角形')
        elif a==b or a==c or b==c:
            print('等腰三角形')
        else:
            print('普通三角形')
    else:
        print('不是三角形')
triangle_test(11,12,13)
"""


def add(num, num1):
    """加法运算"""
    result = num + num1
    return result


# add(12, 23)


def sub(num, num1):
    """减法运算"""
    result = num - num1
    return result


# sub(12, 4)


def mul(num, num1):
    """乘法运算"""
    result = num * num1
    return result


# mul(2, 3)


def div(num, num1):
    """除法运算"""
    result = num / num1
    return result


#  div(4, 2)


def calc(num, num1, num2):
    if num2 == '+':
        result = add(num, num1)
    elif num2 == '-':
        result = sub(num, num1)
    elif num2 == '*':
        result = mul(num, num1)
    elif num2 == '/':
        result = div(num, num1)
        print(result)


calc(4, 3, "/")
