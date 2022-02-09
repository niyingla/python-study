def login():
    username = input('请输入您的用户名')
    password = input('请输入您的密码')
    code = int(input('请输入您的验证码'))
    if username == 'admin' and password == '123456':
        if code == 8888:
            return '登陆成功'
        else:
            return '验证码错误'
    else:
        return '用户名或密码错误'


print(login())
