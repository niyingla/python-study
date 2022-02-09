# 类名 电脑 computer
# 属性 品牌 lenovo 联想 苹果 apple_computer   价格 price
# 方法 播音乐 broadcast_music 播电影 broadcast_movie
class Computer():
    """电脑类"""
    def __init__(self,name,price):
        """设置属性"""
        self.name = name
        self.price = price
    def broadcast_music(self,music):
        print(f'{self.name}播放音乐"{music}"')
    def broadcast_movie(self,move):
        print(f'{self.name}播放电影"{move}"')
lenovo = Computer('联想电脑',5000)
lenovo.broadcast_music('桥边姑娘')
apple_computer = Computer('苹果电脑',10000)
apple_computer.broadcast_movie("骇客帝国")
# 第一个类 房子 house
# 属性 户型 house_type 总面积 total_area 家具名称列表 item_list (新房子没有任何家具) 剩余面积free_area
# 方法 添加家具 add_item
# 第二个类  家具 HouseItem
# 属性 名字 name  占地面积 area
# 根据计算机的家具在前 房子在后
# class HouseItem(object):
#     """家具类"""
#     def __init__(self,name,area):
#         """设置属性"""
#         self.name = name
#         self.area = area
#     def __str__(self):
#         return f'{self.name}占地{self.area}平方'
# bed = HouseItem('席梦思',4)
# chest = HouseItem('衣柜',2)
# table = HouseItem('餐桌',1.5)
# print(bed)
# print(chest)
# print(table)
# class House():
#     """房子类"""
#     def __init__(self,house_type,total_area):
#         self.house_type = house_type
#         self.total_area = total_area
#         self.item_list = []
#         self.free_area = total_area
#     def add_item(self,item):
#         """添置家具面积变了,家具添了"""
#         if self.free_area > item.area:
#             self.total_area -= item.area
#             self.item_list.append(item.name)
#         else:
#             print('添置家具面积大了,空间不足')
#     def __str__(self):
#         return f'户型: {self.house_type} 总面积: {self.total_area} 剩余面积:{self.free_area} 家具名称列表{self.item_list}'
# he = House('别墅',200)
# he.add_item(bed)
# he.add_item(chest)
# he.add_item(table)
# print(he)







