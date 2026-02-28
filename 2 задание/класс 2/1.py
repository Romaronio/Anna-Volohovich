from itertools import *
def f(a,b,c,t):
	return (((not a) or (not b)) and (c <= (not a)) and (t and (not a) or c and (not b)))

table = [(1, 0, 0, 1), (1, 1, 0, 1), (0, 0, 0, 1), (1, 0, 0, 0)]
slovar = {}
for stroka in table:
	for i in permutations('abct'):
		u = zip(i, stroka)
		slovar.update(u)
		print(**slovar)
		if [f(**slovar)] == [0, 1, 0, 1]:
			print(i)