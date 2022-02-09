# 面向对象
#     定义类
# 类名:登录页面 LoginPage
# 属性:用户名 密码 验证码 username password code
# 方法:点击 click_button()
# 面向对象设计
# 定义类
class LoginPage(object):
    """设置属性"""
    def __init__(self,username,password,code=8888):
        """属性设置"""
        self.username = username
        self.password = password
        self.code = code
    def click_button(self):
        if self.username == 'admin'and self.password == '123456':
            if self.code == 8888:
                print('登录成功')
            else:
                print()

        """点击方法"""
        print(f'登录成功,账号:{self.username}密码:{self.password}验证码:{self.code}')
    def __str__(self):
        """这个是打印对象的自定义信息"""
        return '这个是后台登录的测试数据'
test = LoginPage('admin','123456')
test.click_button()
#  str 方法的应用
print(test)
