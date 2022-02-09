"""
sum = 0
for i in range(0,101):
    if i % 2 != 0:
        sum = sum + i
print(f'和为:{sum}')
"""
"""
num = 0
info = 'H-e--l---l--oP---y--t-hon'
for i in info:
    if i == '-':
        num += 1
print(num)
info1 = ['爱', '我', '中', '华']
for i in info1:
    print(i)
"""
"""
info = '少小离家老大回,乡音无改鬓毛衰,儿童相见不相识,笑问客从何处来'
info2 = info.split(',')
print(info2[0])
print(info2[1])
print(info2[2])
print(info2[3])
"""
"""
info = ["刘备", "男", "双股剑"]
info.append('字玄德')
info.insert(0,'武力值100')
info.pop(2)
info.reverse()
for i in info:
    print(i)
print(info)
"""
num = 0
for i in range(0,101):
    if i % 2 == 0:
        num = num + i
        print(num)
num1 = 0
num2 = "H-e--l---l--oP---y--t-hon"
for i in num2:
    if i == 'o':
        num1 = num1 + 1
print(num1)


