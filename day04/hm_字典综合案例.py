"""
person_info = [{"name": "刘备", "age": "45", "title": "蜀国君主"},
              {"name": "张飞", "age": "40", "title": "右将军"},
              {"name": "关羽", "age": "43", "title": "前将军"}]
num = input('请输入要查询的名字：')
for i in person_info:
    if num == i.get('name'):
        print(f'姓名：{i.get("name")},年龄：{i.get("age")},官职：{i.get("title")}')
"""
"""
info_list = []
for i in range(3):
    name = input('输入姓名：')
    age = int(input('输入年龄：'))
    six = input('输入性别：')
    per_info = {'name': name, 'age': age, 'gender': six}
    info2 = info_list.append(per_info)
print(info_list)
"""
# 记录登录功能测试的用例数据
# 列表元素的列表形式
test_data1 = [['admin', '123456', 8888, '登录成功'], ['aaa', '123456', 8888, '用户名和验证码错误'],
              ['admin', '123456', 888, '验证码错误']]
# 列表元素的元组形式
test_data2 = [('admin', '123456', 8888, '登录成功'), ('aaa', '123456', 8888, '用户名和验证码错误'),
              ('admin', '123456', 888, '验证码错误')]
# 列表元素的元组形式
test_data3 = (
    ['admin', '123456', 8888, '登录成功'], ['aaa', '123456', 8888, '用户名和验证码错误'], ['admin', '123456', 888, '验证码错误'])
test_data4 = (
    ('admin', '123456', 8888, '登录成功'), ('aaa', '123456', 8888, '用户名和验证码错误'), ('admin', '123456', 888, '验证码错误'))
# 字典元素的列表形式
test_data5 = [{'username': 'admin', 'password': '123456', 'code': 8888, 'result': '登录成功'},
              {'username': 'aaa', 'password': '123456', 'code': 8888, 'result': '用户名和验证码错误'},
              {'username': 'admin', 'password': '123456', 'code': 888, 'result': '验证码错误'}]
# 遍历测试数据
for i in test_data1:
    print(f'用户名:{i[0]} 密码:{i[1]} 验证码:{i[2]} 期望结果:{i[3]}')
for i in test_data5:
    print(f'用户名:{i.get("username")} 密码:{i.get("password")} 验证码:{i.get("code")} 期望结果:{i.get("result")}')
