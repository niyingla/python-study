# # 捕获异常
# try:
#     num = int(input('请输入数据:'))
#     print(num)
# except:
#     print('请输入正确的数字')
#
# # 捕获特定异常
# try:
#     num = int(input("请输入数据:"))
#     result = 8 / num
#     print(result)
# except ZeroDivisionError:
#     print('除数不能为0')
# 捕获未知异常
# try:
#     num = int(input("请输入数据:"))
#     result = 8 / num
#     print(result)
# except Exception as e:
#     print(f'捕获异常为{e}')
# 总和练习
try:
    num = int(input("请输入数据:"))
except ValueError:
    print("输入的是非数字")
except Exception as e:  # 未知类型错误
    print(f'其他类型错误{e}')
else:  # 上述都不满足
    if num % 2 == 0:
        print('偶数')
    else:
        print('基数')
finally:  # 不管什么结果都执行
    print('程序运行结束')
