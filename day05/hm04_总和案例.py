# 录入单个学生信息:有学生名字,年龄,最后返回结果
def info():
    """录入单个学生的信息"""
    name = input('请输入您的姓名')
    age = int(input('请输入您的年龄'))
    info1 = {'name':name,'age':age}
    return info1

# 因为要展示学生的列表,录入的信息放入到列表找中
list_info = []
for i in range(3):
    """调用录入的函数"""
    result = info()
    list_info.append(result)
print(list_info)
def input_info():
    """展示学生的信息"""
    print('-------学生列表信息-------')
    # 有规律的循环打印,定计数器
    num = 1
    for i in list_info:
        print(f'{num}        {i.get("name")}      {i.get("age")}')
        num += 1
    print('-------------------------')
input_info()
def count_info():
    """统计人数,列表长度"""
    return len(list_info)

# 调用并打印
print(count_info())
def search():
    """查询人员的函数"""
    info2 = input('请输入要查询的学生信息')
    for i in list_info:
        name1 = i.get('name')
        if info2 == name1:
            print(f'姓名:{name1},年龄:{i.get("age")}')
            break
        else:
            print('对不起,名字叫[张三]的学生不存在')
search()
