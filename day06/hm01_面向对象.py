# 面向对象
#     定义类
# 类名:登录页面 LoginPage
# 属性:用户名 密码 验证码 username password code
# 方法:点击 click_button()
# 面向对象设计
# 定义类
class Cat(object):
    """猫类"""
    """初始化方法专门定义有哪些属性"""
    def __init__(self,name,color):
        """定义属性"""
        self.name = name
        self.color = color

    def eat(self):
        """吃方法"""
        print(f'{self.name}是{self.color}的,爱吃鱼')

    def drink(self):
        """喝方法"""
        print(f'{self.name}是{self.color}的,爱喝水')


# 创建对象
xm = Cat('小猫','白色')
tom = Cat('汤姆','灰色')
# 调用方法
xm.eat()  # 调用吃的方法
xm.drink()  # 调用喝的方法
tom.eat()
tom.drink()
# 总结
# 创建对象是,类名后面需要加括号
# 类内部定义方法是,需要缩进,方法需要带self参数
