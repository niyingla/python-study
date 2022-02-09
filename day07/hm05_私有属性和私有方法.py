class Wonme(object):
    """女生类"""

    def __init__(self, name, age):
        """设置属性"""
        self.name = name
        self.__age = age

    def __secret(self):
        """私有方法,输入女生年龄"""
        print(f"{self.name}的年龄是:{self.__age}")

    def friend(self):
        self.__secret() # 类内部直接调用私有方法
        print(f"我闺蜜友叫:{self.name},她的年龄是:{self.__age}")


# 创建对象
w1 = Wonme('小红', 18)
#  w1.__secret() # 不能直接查看:私有方法报错
w1.friend()  # 可以借助普通方法查看私有属性或者私有方法
