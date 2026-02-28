# print('X Y Z W')
# for x in range(2):
# 	for y in range(2):
# 		for z in range(2):
# 			for w in range(2):
# 				if (not(w <= (x == y)) and (z <= x)) == 1:
# 					print(x, y, z, w)


from itertools import *

def f(x, y, z, w):
	return (not(w <= (x == y))) and (z <= x)

for a in product([0, 1], repeat=5):
	table = [(a[0], 0, 1, 0), 
					(0, a[1], a[2], 0),
					(a[3], 1, 1, a[4])
					]
	if len(set(table)) != 3:
		continue

	for i in permutations('xyzw'):
		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
			print(i)