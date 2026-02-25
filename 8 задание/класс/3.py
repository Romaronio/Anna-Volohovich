from itertools import *
k = 0
nomer = 0
for w in product('мужчина', repeat=6):
	nomer += 1
	print(w)
	s = ''.join(w)
	if s[0] != 'ж' and s.count('ч') < 2 and nomer % 2 == 0:
		k += 1
print(k)