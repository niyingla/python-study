"""
has_ticket = True
knife_length = 17
if has_ticket:
    if knife_length > 20:
        print('不许上车')
    else:
        print('安检通过')
else:
    print('没有门票,不允许进门')
"""
"""
import random
people = int(input('请出拳可以选择石头(1),剪刀(2),布(3):'))
computer = random.randint(1,3)
if (people == 1 and computer == 2) or (people == 2 and computer == 3) or(people == 2 and computer == 1):
    print('人真厉害,赢了')
elif people == computer:
    print('真是心意相通,出的一样哈')
else:
    print('电脑太厉害了')
"""
"""
num = int(input('请输入一个数字'))
if num % 2 == 0:
    print('结果是偶数')
else:
    print('结果是基数')
"""
"""
weight = int(input('请输入您的体重:'))
if 0 < weight < 500:
        print('停止减肥')
    elif 40 <= weight <= 45:
        print('每天晨跑30分钟')
    elif 45 <= weight <= 50:
        print('每天健身房1小时')
    elif 50 <= weight <= 60:
        print('每天健身房2小时')
    elif 60 <= weight <= 80:
        print('两餐素质,每天健身房3小时')
    elif weight > 80:
        print('爱咋咋地吧,你开心就好!')
else:
print('超出范围')
"""
"""
num = 1
while num <= 10:
    print('Hello Python')
    num += 1
"""
"""
num = 1
while num <= 10:
    print('Hello Python', end=' \t')
    num += 1
"""
"""
num = 10
while 10 <= num <= 20:
    print(num)
    num += 1
"""
"""
while True:
    num = int(input('请输入一个数字:'))
    if num == 110:
        break
"""
"""
triangle_side1 = int(input('请输入三角形的第一边:'))
triangle_side2 = int(input('请输入三角形的第二边:'))
triangle_side3 = int(input('请输入三角形的第三边:'))
if (triangle_side1 + triangle_side2 > triangle_side3) or (triangle_side2 + triangle_side3 > triangle_side1) or (
        triangle_side1 + triangle_side3 > triangle_side2):
    if (triangle_side1 == triangle_side2 != triangle_side3) or (triangle_side1 == triangle_side3 != triangle_side2) or (
            triangle_side2 == triangle_side3 != triangle_side1):
        print('等腰三角形')
    elif triangle_side1 == triangle_side2 == triangle_side3:
        print('等边三角形')
    else:
        print('普通三角形')
else:
    print('不是三角形')
"""

import random
num = 1
num2 = random.randint(0, 10)
while True:
    num1 = int(input('请输入一个数字:'))
    if num1 == num2:
        print(f'猜测次数{num}')
        break
    elif num1 > num2:
        print('猜大了')
    else:
        print('猜小了')
    num += 1