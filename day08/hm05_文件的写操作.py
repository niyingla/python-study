# 写入信息到文件 readme1.txt
# 1.打开文件
# file = 'test_file/readme1.txt'
# with open(file, mode='w', encoding='utf-8') as f:
#     # 2.操作文件:写入
#     f.write('百日依山尽,\n黄河入海流.\n欲穷千里目,\n更上一层楼.\n')
#     f.write('春眠不觉晓')


#
file = 'test_file/readme2.txt'
# 定义要写入的数据
info = ['百日依山尽\n','黄河入海流\n','欲穷千里目\n','更上一层楼\n']
with open(file, mode='w', encoding='utf-8') as f:
    # 2.操作文件:写入
    f.writelines(info)
    # 3.尾部追加
    f.write('春眠不觉晓\n')
