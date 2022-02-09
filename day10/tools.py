class Animal(object):
    type = "狗"

    def __init__(self, name):
        self.name = name
        self.__age = 0

    def eat(self):
        print(f"{self.type}吃骨头")


g = Animal('倪倪')


