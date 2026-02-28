from itertools import *
k = 0
for w in product(sorted('сумка'), repeat=5):
	k += 1
	s = ''.join(w)
	if s == 'кумас':
		print(k, s)
		break
	