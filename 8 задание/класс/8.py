from itertools import *
k = 0
for w in product('взгляд', repeat=4):
	s = ''.join(w)
	if s.count('з') == 1 or s.count('з') == 2:
		k += 1
		print(k, s)
		
	