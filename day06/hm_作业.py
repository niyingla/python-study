# 类名字 儿童 child
# 方法 吃 eat 喝 drink 运动 exercise
# class Child(object):
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f'{self.name}在吃东西')
#     def drink(self):
#         print(f'{self.name}在喝东西')
#     def exercise(self):
#         print(f'{self.name}在运动')
# chi = Child('小明')
# chi.eat()
# he = Child('小明')
# he.drink()
# yd = Child('小明')
# yd.exercise()
# 类名 水果 fruits
# 属性 苹果 apple 橘子 orange 西瓜 watermelon  颜色 color 价格 price
class Fruits(object):
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def __str__(self):
        return f"{self.name}是{self.color}的, 价格是:{self.price}元"
apple = Fruits('苹果','红色',3)
orange = Fruits('橘子','黄色',2)
watermelon = Fruits('西瓜','绿色',5)
print(apple)
print(orange)
print(watermelon)



