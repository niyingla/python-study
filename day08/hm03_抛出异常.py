# 代码抛出异常
def input_password():
    pwd = input('请输入密码:')
    if len(pwd) < 8:
        """抛出异常"""
        ex = Exception('密码长度小于8位数')
        raise ex
    else:
        return pwd


print(input_password())
# 结论
# 当密码长度不足8位时抛出的异常信息:Exception: 密码长度小于8位数
