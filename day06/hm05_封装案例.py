# 封装
# 设计类
class LoginPage(object):
    """登录页面类"""

    def __init__(self, username, password, code):
        """设置属性"""
        self.username = username
        self.password = password
        self.code = code

    def click_button(self):
        """登录方法"""
        print(f'请输入用户名:{self.username}')
        print(f'请输入用户名:{self.password}')
        print(f'请输入用户名:{self.code}')
        print('点击登录按钮')


dl = LoginPage('admin', '123456', 8888)
dl.click_button()
