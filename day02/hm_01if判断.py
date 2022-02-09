"""
age = int(input('请输入您的年龄:'))
# 判断:有个表达记过是布尔值
# if和else成对出现的,else不能单独使用
if age >= 18:
    print('可以进入网吧玩了哈')
else:
    print('就不能进去了,回家做作业吧!')
print('看看我能显示出来吗')
"""
"""
and的判断条件
age = int(input('请输入您的年龄:'))
# if age > 0 and age <120:
if 0 > age < 120:
    print('年龄显示正确')
else:
    print('年龄显示错误')
"""
# or的判断条件

python_score = 30
c_score = 80
if python_score > 60 or c_score > 60:
    print('成绩合格了')
else:
    print('成绩不合格')

# not 的判断
"""
is_employee = False
if not is_employee:
    print('允许入内')
else:
    print('不允许入内')
    """

