# 小明今天18岁了
"""
name = '小明'
age = 18
print("{}今年{}岁了".format(name, age))
print(name + "今年" + str(age) + "岁了")
print(f'{name}今年{age}岁了')
print(f'{name}今年{age + 1}岁了')
"""
# 格式化符号输出
# %d 表示整数
# %s 表示字符串 %.2f保留两位小数
# %f 表示浮点数
# %% 表示%自己
"""
name = '小明'
age = 18
height = 1.70
score = 90
print("%s的身高是%.2f" % (name, height))
print('及格率为%d%%' % score)
"""
# 转义字符
# 我的名字是:小明
name = '小明'
print("我的名字是: ", name, end=" ")
print("我的名字是:%s" % name, end=" ")
print("我的名字是:小明", end="\t")
