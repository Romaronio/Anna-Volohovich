from itertools import *
k = 0
for w in product('0123456', repeat=5):
	s = ''.join(w)
	for i in '0123456':
		s = s.replace(2 * i, '9')
	if '9' not in s and s.count('6') == 1 and s[0] != '0':
			k += 1
			print(s)
print(k)