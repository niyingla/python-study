def info():
    name = input('请输入学生的姓名')
    age = int(input('请输入学生的年龄'))
    dict_info = {'name':name,"age":age}
    return dict_info
list_info = []
for i in range(3):
    result = info()
    list_info.append(result)
def show_info():
    print('------学生列表信息------')
    num = 1
    for i in list_info:
        print(f'{num}     {i.get("name")}    {i.get("age")}')
        num += 1
show_info()
def count_info():
    return len(list_info)
print(count_info())
def scr():
    info2 = input('请输入要查询的学生姓名')
    for i in list_info:
        if info2 == i.get('name'):
            print(f'姓名:{i.get("name")},年龄:{i.get("age")}')
            break
    else:
        print('对不起  ')
scr()






