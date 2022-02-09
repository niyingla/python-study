class Child(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f'{self.name}在吃东西')
    def drink(self):
        print(f'{self.name}在喝东西')
    def exercise(self):
        print(f'{self.name}在运动')
chi = Child('小明')
chi.eat()
he = Child('小明')
he.drink()
yd = Child('小明')
yd.exercise()
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
class Computer():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def broadcast_music(self,music):
        print(f'{self.name}播放音乐"{music}"')
    def broadcast_movie(self,move):
        print(f'{self.name}播放电影"{move}"')
lenovo = Computer('联想电脑',5000)
lenovo.broadcast_music('桥边姑娘')
apple_computer = Computer('苹果电脑',10000)
apple_computer.broadcast_movie("骇客帝国")
