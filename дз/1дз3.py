a = int(input('введите число a'))
b = int(input('введите число b'))
c = int(input('введите число c'))
D = b ** 2 - 4 * a * c
if D < 0:
    print('нет решений')
if D == 0:
    x = -b/(2*a)
    print('x=',x)
if D > 0:
    x = (-b+D**0.5)/(2*a)
    y = (-b-D**0.5)/(2*a)
    print('x=',x)
    print('y=',y)