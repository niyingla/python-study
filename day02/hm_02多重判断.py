# 判断多个条件,多个结果
"""
score = int(('请输入您的分数'))
if score >= 90:
    print('良')
elif 80 <= score < 90:
    print('优')
elif 70 <= score < 80:
    print('良')
elif 60 <= score < 70:
    print('差')
else:
    print('不及格')
"""
# if 的嵌套 有严格的缩进
"""
has_ticket = True
knife_length = 19
if has_ticket:
    if knife_length > 20:
        print('安检不通过')
    else:
        print('安检通过')
else:
    print('不允许上车')
"""
# 扩展
has_ticket = int(input('输出0无票,输入数字非0有票'))
if has_ticket:
    knife_length = int(input('请输入刀的长度'))
    if knife_length > 20:
        print('安检不通过')
    else:
        print('安检通过')
else:
    print('不允许上车')