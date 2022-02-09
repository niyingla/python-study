class SweetPotato(object):
    """地瓜类"""
    def __init__(self,):
        """实例属性"""
        self.state = "生的"
        self.cooked_time = 0
    def __str__(self):
        """打印对象的自定义信息"""
        return f'地瓜状态为:{self.state},烧烤总时间为:{self.cooked_time}分钟'
    def cook(self,time):
        self.cooked_time += time
        """判断状态"""
        if 0 <= self.cooked_time < 3:
            self.state = '生的'
        elif 3 <= self.cooked_time < 6:
            self.state = '半生不熟'
        elif 6 <= self.cooked_time < 8:
            self.state = '熟了'
        elif self.cooked_time > 8:
            self.state = '烤糊了'
# 创建对象
time1 = SweetPotato()
# 调用方法
time1.cook(2)
time1.cook(5)
# 打印地瓜对象
print(time1)