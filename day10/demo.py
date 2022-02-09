from day10.tools import Animal


class Dag(Animal):
    def eat(self):
        super().eat()
        print('吃完骨头瑶瑶头....')


g1 = Dag('小花')
g1.eat()

