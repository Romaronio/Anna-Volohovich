from itertools import *
def f(x, y, z, w):
	return ((x <= y) or (z <= w)) and (not(x <= w))

for a in product([0, 1], repeat=5):
	table = [(0, a[0], 0, a[1]), (1, 0, 0, a[2]), (a[3], 0, a[4], 1)]
	if len(set(table)) != 3:
		continue
	for i in permutations('xyzw'):
		if [f(**dict(zip(i, stroka))) for stroka in table] == [1, 1, 1]:
			print(i)