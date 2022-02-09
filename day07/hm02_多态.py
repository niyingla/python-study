# 多态 案列
class Person(object):
    def work(self):
        print("人类需要工作")
class Coder(Person):
    def work(self):
        print('程序员的工作主要是:"写代码"')
class Designer(Person):
    def work(self):
        print("设计师的工作方法主要是:'画图纸'")
# 创建对象
coder = Coder()

designer = Designer()
# 调用工作方法
coder.work()
designer.work()
# 结论 不同对象调用相同类方法,产生不同的执行结果

# 多态案例
class Dog(object):
    """"狗类"""
    def __init__(self,name):
        self.name = name
    def game(self):
        print(f"{self.name}只会简单玩耍")
class XiaoTianQuan(Dog):
    """哮天犬类"""
    def game(self):
        """重写父类的方法"""
        print(f"{self.name}在天山玩耍")
xh = Dog('小黄')
xyq = XiaoTianQuan('天神')

class Person(object):
    def play_with_dog(self,dog):  #  dog相当于任意一个对象
        """和狗玩耍的方法"""
        dog.game()   # 狗类对象调用相同的game方法  xh.game  xyq.game
per = Person()
per.play_with_dog(xh)
per.play_with_dog(xyq)


