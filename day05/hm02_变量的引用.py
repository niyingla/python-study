# 局部变量
def login_front():
    """前台登录"""
    username = '18903776820'
    password = '123456'
    print(username, password)


def login_back():
    """后台登录"""
    username = 'admin'
    password = '123456'
    print(username, password)


if __name__ == '__main__':
    login_back()
    login_front()
# 全局变量的修改
num = 100


def demo1():
    print(f'值1为:{num}')


def demo2():
    global num  # 全部变量的修改
    num = 200
    print(f'值2为:{num}')


if __name__ == '__main__':
    demo1()
    demo2()
