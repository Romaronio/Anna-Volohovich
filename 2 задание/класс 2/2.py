from itertools import *
def f(x, y , z, w):
	return (((x <= y) or (z <= w)) and (not(x <= w)))

for a in product([0, 1], repeat=5):
	table = [(0, a[0], 0, a[1]), (1, 0, 0, a[2]), (a[3], 0, a[4], 1)]
	if len(set(table)) != len(table):
		continue

F = [1, 1, 1]

for p in permutations('xyzw'):
	flag = True 
	for i in range(len(table)):
		stroka = table[i]
		x = stroka[p.index('x')]
		y = stroka[p.index('y')]
		z = stroka[p.index('z')]
		w = stroka[p.index('w')]
		print(f(x, y, z, w))
		if f(x, y, z, w) != F[i]:
			flag = False
			break
	if flag == True:
		print(i)