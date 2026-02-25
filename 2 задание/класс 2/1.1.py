# from itertools import *
# def f(a,b,c,t):
# 	return (((not a) or (not b)) and (c <= (not a)) and (t and (not a) or c and (not b)))

# table = [(1, 0, 0, 1), (1, 1, 0, 1), (0, 0, 0, 1), (1, 0, 0, 0)]

# for i in permutations('abct'):
# 	if [f(**dict(zip(i, stroka))) for stroka in table] == [0, 1, 0, 1]:
# 		print(i)


from itertools import permutations

def F(a, b, c, t):
    return ((not a or not b) and (c <= (not a)) and (t and not a or c and not b))

# Исходные строки (порядок столбцов неизвестен)
rows = [
    (1, 0, 0, 1),
    (1, 1, 0, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 0)
]

# Ожидаемые значения F для этих строк
expected = [0, 1, 0, 1]

# Перебираем все возможные порядки столбцов
for perm in permutations('abct'):   # например, ('a','b','c','t')
    match = True
    for i in range(len(rows)):
        row = rows[i]
        # Извлекаем значения переменных согласно их позициям в perm
        a = row[perm.index('a')]
        b = row[perm.index('b')]
        c = row[perm.index('c')]
        t = row[perm.index('t')]
        if F(a, b, c, t) != expected[i]:
            match = False
            break
    if match:
        print(''.join(perm))
        break