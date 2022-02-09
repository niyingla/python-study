# 导包(随机数包)
# import random
#
# # a = random.randint(26,30)
# # print(a)
# player = int(input('请出拳输入数字(石头1),(剪刀2),(步3):'))
# computer = random.randint(1, 3)
# if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#     print('人胜利了')
# elif player == computer:
#     print('心有灵犀,再来一把')
# else:
#     print('电脑太厉害了')
num = 1
import random
num1 = random.randint(0,10)
try:  # 捕获未知异常
    while True:
        print(f'猜测次数{num}')
        num2 = int(input('请输入一个数字:'))
        if num2 == num1:
            input('猜对了')
        elif num2 > num1:
            print('猜大了')
        else:
            print('猜错了')
        num += 1
except Exception as f:
    print('出现的异常结果是{}'.format(f))  # 出现异常时候显示 不是数字的时候