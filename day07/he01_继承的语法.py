# #  案例继承
# class Animal(object):
#     """动物类"""
#     def __init__(self,name,age):
#         """设置属性"""
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f'{self.name}吃东西')
#
#     def sleep(self):
#         print(f"{self.name}要睡觉")
# class Cat(Animal):
#     """猫类"""
#     def catch(self):
#         """抓老鼠"""
#         print(f"{self.name}会抓老鼠")
# class Dog(Animal):
#     """"狗类"""
#     def look_door(self):
#         print(f"{self.name}会看门")
# class XiaoTianQuan(Dog):
#     """哮天犬类"""
#     def fly(self):
#         """飞的方法"""
#         print(f"{self.name}会飞")
# #  创建对象
# tom = Cat("汤姆",3)
# xtq = XiaoTianQuan("天神",100)
# """调用方法"""
# tom.catch()
# xtq.fly()

# 问题:猫只吃鱼 方法的重写 覆盖式重写
# class Animal(object):
#     """动物类"""
#     def __init__(self,name,age):
#         """设置属性"""
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f'{self.name}吃东西')
#
#     def sleep(self):
#         print(f"{self.name}要睡觉")
# class Cat(Animal):
#     """猫类"""
#     def eat(self):
#         print(f"{self.name}喜欢吃鱼")
# tom = Cat("汤姆",3)
# tom.eat()

# 问题:猫吃东西 方法的重东西,更喜欢吃鱼 扩展式重写

class Animal(object):
    """动物类"""
    def __init__(self,name,age):
        """设置属性"""
        self.name = name
        self.age = age
    def eat(self):
        print(f'{self.name}吃东西')

    def sleep(self):
        print(f"{self.name}要睡觉")
class Cat(Animal):
    """猫类"""
    def eat(self):
        super().eat()
        print(f"{self.name}更喜欢吃鱼")
tom = Cat("汤姆",3)
tom.eat()












