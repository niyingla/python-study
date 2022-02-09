"""
list_info = []
for i in range(3):
    fruits = input('请输入水果的名称:')
    price = float(input('请输入水果的价格:'))
    info = {'fruits': fruits, 'price': price}
    result = info
    list_info.append(result)
def show_info():
    num = 1
    for i in list_info:
        print(f'{num}     {i.get("fruits")}     {i.get("price")}' )
        num += 1
show_info()
"""
def data(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

data(2012)
print(data(2012))
