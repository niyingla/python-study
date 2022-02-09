# import os
# info = os.path.dirname(__file__)
# print(info)







# num = 1
# result = 0
# while num <= 100:
#     result = result + num
#     num += 1
# print(result)

# result = 0
# for i in range(101):
#     result = result + i
# print(result)

# 九九乘法表
# for i in range(1,10):
#     for f in range(1,i+1):
#         print(f"{f}x{i}= {f*i}",end="")
#     print()
for i in range(1,10):
    for f in range(1,i+1):
        print("*",end = "")
    print()