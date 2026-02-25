from itertools import *
k = 0
for w in product('кресло', repeat=4):
	s = ''.join(w)
	if s[0] in 'крсл' and s[-1] in 'ое':
		k += 1
		print(w, k)