# def f(x, y, z):
#     return (not(x == y <= z))
# from itertools import *
# for a in product([1, 0], repeat=5):
#     table = [(0, 0, 1), (0, 1, 1)]
#     if len(set(table)) == 2:
#         for i in permutations('xyz'):
#             if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 0]:
#                 print(i)
#
#
#
# def f(x, y, z, w):
#     return ((y or (not(z))) and not(z == w) and not(x))
# from itertools import *
# for a in product([1,0], repeat=4):
#     table = [(1, 1, a[0], a[1]), (a[2], 1, 0, 0), (1, a[3], 1, 0)]
#     if len(set(table)) == 3:
#         for i in permutations('xyzw'):
#             if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
#                 print(i)



def f(x, y, z, w):
    return (((x <= y) or (z == x)) and (w <= z))
from itertools import *
for a in product([0, 1], repeat=0):
    table = [(0, 0, 1, 1), (0, 0, 1, 0), (0, 1, 1, 1)]
    if len(set(table)) == 3:
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 0, 0]:
                print(i)