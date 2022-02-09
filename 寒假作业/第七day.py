"""
class Person(object):

    def __init__(self, name):
        self.name = name


p1 = Person('张三')
p2 = Person('李四')
p3 = Person('王五')
p4 = Person('赵六')


class Bus(object):

    def __init__(self, type_name, seat_count):
        self.type_name = type_name
        self.seat_count = seat_count
        self.member_list = []

    def __str__(self):
        return f'类型{self.type_name},座位数{self.seat_count},乘客列表{self.member_list}'

    def add_bus(self, po):
        if self.seat_count > 0:
            self.member_list.append(po.name)
            self.seat_count -= 1
            print(f'类型{self.type_name},座位数{self.seat_count},乘客列表{self.member_list}')
        else:
            print('已经没有剩余座位了')

    def sub_bus(self, po):
        for i in self.member_list:
            if i == po.name:  # 列表中的人名字和要求传入的一致
                self.member_list.remove(po.name)
                self.seat_count += 1
                break  # 如果人存在直接结束循环
        else:
            print('车上已没有这个人')
        print(f'类型{self.type_name},座位数{self.seat_count},乘客列表{self.member_list}')


he = Bus('巴士', 50)
he.add_bus(p1)
he.add_bus(p2)
he.add_bus(p3)
he.add_bus(p4)
print(he)
he.sub_bus(p1)
he.sub_bus(p1)
"""
class Coder(object):

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

