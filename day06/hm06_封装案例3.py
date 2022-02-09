# 分析:摆放家具
# 1,设计类 两个类
# 类名: House
# # 属性: 户型 house_type,总面积 total_area,家具名称列表 item_list
# 方法: 添加 add_item
# 2,家具第二个类
# 类名: HouseItem
# 属性: 家具名称 name,家具面积 area
# 3,两个类之间的关系? 先家具,后面是房子
class HouseItem(object):
    """家具的类"""

    def __init__(self, name, area):
        """设置属性"""
        self.name = name  # 家具名称
        self.area = area  # 家具面积

    def __str__(self):
        """自定义对象信息"""
        return f'{self.name}占地{self.area}平米'



# 创建对象
bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)
print(bed)
print(chest)
print(table)

class House(object):
    """房子类"""
    def __init__(self,house_type,total_area):
        """房子设置属性"""
        self.houae_type = house_type  # 户型
        self.total_area = total_area  # 总面积
        self.item_list = []    # 房子对象创建时,家具列表默认就是空的
        self.free_area = total_area  # 房子对象创建时,剩余面积默认总面积
    def add_item(self,item):
        """"添加家具方法"""
        # 怎么天机家具,剩余面积会变化,家里劫镖与元素增加
        # 判断 家具能否添加,面积够不够
        if self.free_area > item.area:
            self.free_area -= item.area
            self.item_list.append(item.name)
        else:
            print('家具面积过大,无法添加成功')
    def __str__(self):
        return f'户型:{self.houae_type} 总面积:{self.total_area} 剩余面积:{self.free_area} 家具列表:{self.item_list}'
h1 = House('别墅',200)
h1.add_item(bed)
h1.add_item(chest)
h1.add_item(table)
# 打印房子对象
print(h1)