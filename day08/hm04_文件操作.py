# 文件路径
# 相对路径 ../test_file/readme.txt
# 绝对路径
# import os
# # 查看当前文件的绝对路径(__file__:表示当前的文件)
# file_dir = os.path.dirname(__file__)
# print(file_dir)  绝对路径:file_dir + '/test_file/readme.txt ' # 当前py文件的绝对路径
# 找到被打开的文件
# file = "test_file/readme.txt"
# # 文件的读取
# # 读取readme.txt 文件的所有内容
# # 1,打开文件
# with open(file, mode="r", encoding='utf-8') as f:
#     # 2,操作文件:读取
#     test = f.read()
#     print(test)
# 3,关闭文件(with open会自动关闭

# 单行获取
file = "test_file/readme.txt"
# 文件的读取
# 读取readme.txt 文件的所有内容
# 1,打开文件
with open(file, mode="r", encoding='utf-8') as f:
    # 2,操作文件:读取一行
    test = f.readline()
    print(test)
# 3,关闭文件(with open会自动关闭









# 循环读取
file = "test_file/readme.txt"
# # 文件的读取
# # 1,打开文件
with open(file, mode="r", encoding='utf-8') as f:
    while True:
    # 2,操作文件:循环读取
        test = f.readline()
        print(test,end="")
        if not test:
            break
# # 结论
# # readline()会自动黄,默认只读取第一行,可以进行循环获取并判断