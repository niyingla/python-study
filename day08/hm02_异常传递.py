# 异常传递
def demo():
    num = int(input('请输入一个数字'))  # 1.正在出现异常的地方
    return num


def demo2():
    """调用demo1"""
    print(demo())  # 2.传递到这来


if __name__ == '__main__':
    try:
        demo2()
    except Exception as e:  # 3.最后传递到主程序结束
        print(f"出现的异常{e}")
