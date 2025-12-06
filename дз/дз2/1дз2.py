x = input('введите строку')
y = x.split(' ')
z = max(y, key=len)
print(z)