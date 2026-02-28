# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x <= y) and z and (not(w))) == 1:
#                     print(x, y ,z, w)

#
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x or y) and (not(y == z)) and (not(w))) == 1:
#                     print(x, y, z, w)



# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = ((x or y) <= z) or (y == w) or z
#                 if F == 0:
#                     print(x, y, z, w)


# def f(x, y, z, w):
#     return (not((not(z <= y)) or (x == w) or x))
# from itertools import *
# for a in product([0, 1], repeat=7):
#     table = [
#         (0, 0, a[0], a[1]),
#         (a[2], a[3], 1, a[4]),
#         (a[5], 1, 0, a[6])
#     ]
#     if len(set(table)) == 3:
#         for i in permutations('xyzw'):
#             if [f(**dict(zip(i, stroka))) for stroka in table] == [1,0,0]:
#                 print(i)



# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((not(x <= y)) or (z == w) or z) == 0:
#                     print(x, y, z, w)


# def f(x, y, z, w):
#     return ((not(x <= y)) or (z == w) or z)
# from itertools import *
# for a in product([0, 1], repeat=7):
#     table = [
#         (0, 0, a[0], a[1]),
#         (a[2], a[3], 1, a[4]),
#         (a[5], 1, 0, a[6])
#     ]
#     if len(set(table)) == 3:
#         for i in permutations('xyzw'):
#             if [f(**dict(zip(i, stroka))) for stroka in table] == [0,0,0]:
#                 print(i)







# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F = (y or (not(z)) and (not(z == w)) and (not(x)))
#                 if F == 1:
#                     print(x, y, z, w, F)


def f(x, y, z, w):
    return (y or (not(z)) and (not(z == w)) and (not(x)))
from itertools import *
for a in product([0, 1], repeat=4):
    table = [
        (1, 1, a[0], a[1]),
        (a[2], 1, 0, 0),
        (1, a[3], 1, 0)
    ]
    if len(set(table)) == 3:
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
                print(i)


# x y z w
# 0 0 0 1
# 0 1 0 0 !
# 0 1 0 1
# 0 1 1 0
# 0 1 1 1 !
# 1 1 0 0
# 1 1 0 1
# 1 1 1 0 !
# 1 1 1 1