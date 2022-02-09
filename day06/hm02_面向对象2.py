# 类名字:Dog
# 属性:姓名 颜色 name color
# 方法: 叫 摇尾巴 bark() shake()
class Dog(object):
    """狗的类"""

    def __init__(self, name, color):
        """设置属性"""
        self.name = name  # 名字属性
        self.color = color  # 颜色属性
        pass

    def bark(self):
        """狗叫的方法"""
        print(f'{self.color}的{self.name}汪汪叫')

    def shake(self):
        """摇尾巴方法"""
        print('见到主人摇尾巴')


dh = Dog('大黄', '灰色')
dh.bark()
dh.shake()
