from itertools import *
k = 0
for w in permutations('0123456789', r=4):
	s = ''.join(w)
	for x in '02468':
		for y in '02468':
			s = s.replace(x + y, '*')
	for z in '13579':
		for w in '13579':
			s = s.replace(z + w, '*')
	print(s)
	if '*' not in s and s[0] != '0':
		k += 1
print(k)















