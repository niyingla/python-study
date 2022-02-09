# info = 'hellohema'
# for i in info:
#     print(i)
#     if i == "o":
#         print('可以停止了')
#         break
# for i in range(1, 11):
#     print('肚子有点疼呀呀')
# 需求 计算0-100之间所有的累加和
# for循环实现
result = 0 # 初始计算的结果
for i in range(1,101):  # i 代表从容器把1-100的值一个一个拿出来
    result = result + i
print(f'和为:{result}')


