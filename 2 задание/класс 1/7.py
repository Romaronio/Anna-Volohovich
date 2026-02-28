# print('X Y Z W')
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if ((not(w)) and (y or z <= y and (not(z)))) == 1:
# 					print(x, y, z, w)


# def f(x, y, z, w):
# 	return ((not(w)) and (y or z <= y and (not(x))))
# from itertools import *
# for a in product([1, 0], repeat=8):
# 	table = [(a[0], a[1], a[2], 1), (a[3], a[4], 1, a[5]), (a[6], 1, 1, a[7])]
# 	if len(set(table)) == 3:
# 		for i in permutations('xyzw'):
# 			if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
# 				print(i)













def f(x, y, z, w):
    return ((y or (not(z))) and not(z == w) and not(x))
from itertools import *
for a in product([1,0], repeat=4):
    table = [(1, 1, a[0], a[1]), (a[2], 1, 0, 0), (1, a[3], 1, 0)]
    if len(set(table)) == 3:
        for i in permutations('xyzw'):
            if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
                print(i)






