from itertools import *
k = 0
for w in permutations('ярослав', r=5):
	s = ''.join(w)
	print(s)
	for i in 'рслв':
		s = s.replace(i, 'S')
	for i in 'яао':
		s = s.replace(i, 'G')
	if 'GG' not in s and s.count('S') > s.count('G'):
		print(s)
		k += 1
print(k)