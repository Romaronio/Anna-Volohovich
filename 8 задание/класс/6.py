from itertools import *
k = 0
for w in product(sorted('макс'),repeat=6):
	k += 1
	s = ''.join(w)
	s = s.replace(2 * 'к', '*')
	if '*' not in s and s.count('с') == 0 and s.count('м') == 0:
		print(k, s)
