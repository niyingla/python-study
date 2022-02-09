"""
info1 = ['爱', '我', '中', '华']
for i in info1:
    print(i)
for i in range(10,21):
    print(i)
result = 0
for i in range(100):
    if i % 2 != 0:
        result += i
print(result)
info = "H-e--l---l--oP---y--t-hon"
num = 1
for i in info:
    if i == "-":
        num += 1
print(num)
"""
"""
info = '少小离家老大回,乡音无改鬓毛衰,儿童相见不相识,笑问客从何处来'
info2 = info.split(',')
print(info2[0])
print(info2[1])
print(info2[2])
print(info2[3])
"""
info = ["刘备", "男", "双股剑"]
info.append('字玄德')
info.insert(0, '武力值100')
info.pop(2)
info.reverse()
for i in info:
    print(i)
print(info)
