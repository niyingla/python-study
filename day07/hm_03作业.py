# 有人才上车,人在前
class Person(object):
    """乘客类"""

    def __init__(self, name):
        """设置乘客实例属性"""
        self.name = name


p1 = Person('张三')
p2 = Person('李四')
p3 = Person('王五')
p4 = Person('赵六')


class Bus(object):
    """车类"""

    def __init__(self, type_name, seat_count):
        """设置车的实例属性"""
        self.type_name = type_name
        self.seat_count = seat_count
        self.member_list = []

    def __str__(self):
        return f'类型{self.type_name},座位数{self.seat_count},乘客列表{self.member_list}'

    def add_bus(self, po):
        """上车方法"""
        if self.seat_count > 0:
            self.member_list.append(po.name)
            self.seat_count -= 1
            print(f'类型{self.type_name},座位数{self.seat_count},乘客列表{self.member_list}')
        else:
            print('已经没有剩余座位了')

    def sub_bus(self, po):
        """下车方法"""
        """判断乘客是否存在"""
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
