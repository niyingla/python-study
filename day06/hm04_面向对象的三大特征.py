# 封装案例
# 通过面向对像的设计方法实现如下
# 需求： • 小明 体重 75.0 公斤 •
# 小明每次 跑步 会减肥 0.5 公斤 •
# 小明每次 吃东西 体重增加 1 公斤
# 封装案例一：小明爱跑步 案例演练
# 设计类
# 类名 : 人类--Person
# 属性: 姓名 体重 -- name,weight
# 方法: 跑步 吃 --run() eat()
class Person(object):
    """设置属性"""

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        """跑步方法"""
        """让体重减轻0.5"""
        self.weight -= 0.5

    def eat(self):
        """吃方法"""
        """让体重增加1"""
        self.weight += 1

    def __str__(self):
        """打印对象的信息"""
        return f'{self.name}现在的体重是:{self.weight}'


xm = Person('小明', 75.0)
xmi = Person('小美',45)
# 调用方法
xm.eat()
xm.run()
xmi.eat()
xmi.run()

print(xm)
print(xmi)
