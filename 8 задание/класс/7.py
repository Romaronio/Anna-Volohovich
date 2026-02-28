from itertools import *
k = 0
for w in product(sorted('сентябрь'), repeat=5):
	k += 1
	s = ''.join(w)
	if s[0] == 'р' and s.count('ь') == 0 and k % 2 == 0:
		print(k, s) 
	