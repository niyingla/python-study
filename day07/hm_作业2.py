class Coder(object):
    """程序员类"""

    def __init__(self, title):
        self.__money = 0
        self.title = title

    def work(self):
        self.__money += 10000
        print(f'{self.title}的工作是写代码,工作一次增加{self.__money}')

    @staticmethod
    def sleep():
        print("睡觉比较晚...")

    def __imagine(self):
        print(f"{self.title}幻想有一笔存款:{self.__money * 2}")

    def friend(self):
        self.__imagine()
        print(f"我朋友是{self.title},他幻想有一笔{self.__money * 2}")


xm = Coder('测试员')
xm.work()
Coder.sleep()
xm.friend()


class Rookie(Coder):
    def work(self):
        print(f"{self.title}的工作是打酱油")


djy = Rookie('菜鸟')
djy.work()


class God(Coder):
    def work(self):
        super().work()
        print(f'{self.title}的写代码飞快')


ds = God('大神')
ds.work()
