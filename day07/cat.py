# 导入模块 animal模块
from day07.animal import Ainmal


# 定义类
class Cat(Ainmal):
    """猫类"""

    def __str__(self):
        """自定义对象方法"""
        return f"我是一只猫,名字叫:{self.name}"

    def play(self):
        """玩耍方法"""
        print(f'{self.name}在玩耍')

    @staticmethod
    def run():
        """静态方法"""
        print('动物们跑起来')



tom = Cat('汤姆')
tom.play()
Cat.run()
# 打印tom对象
print(tom)
