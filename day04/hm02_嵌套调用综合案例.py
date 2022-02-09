def input_username():
    username = input('请输入您的用户名:')
    return username
def input_password():
    password = input('请输入您的密码:')
    return password
def login():
    input_username()
    input_password()
    user = input_username
    paw = input_password
    if user == 'admin' and paw == '123456':
        print('登录成功')
    else:
        print('用户名或密码错误')
login()