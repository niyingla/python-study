# 类属性   类方法
# 每件工具都要自己的名字 ----> 每个工具的名字不一样
# 创建了多少个工具对象  --->记录工具类里面工具的数量
class Tools(object):
    """工具类"""
    """"类属性"""
    count = 0  # 类属性名 = 属性值

    def __init__(self, name):
        """设置实例属性"""
        self.name = name
        """递增记录工具数量"""
        Tools.count += 1

    @classmethod
    def show_tool_count(cls):
        """类方法:统计工具数量(类属性)"""
        print(f'工具总共的数量为:{cls.count}')


# 创建对象 (init方法在创建对象的时间自动被调用)
t1 = Tools('斧头')
t2 = Tools('扳手')
t3 = Tools('锤子')
print(f"工具类总数量为{Tools.count}")
# 确认实例属性和类属性
# 如何计算工具数量  (借助init方法)
# 调用方法
Tools.show_tool_count()

# 类方法
