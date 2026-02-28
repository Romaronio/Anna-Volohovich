from itertools import *
k = 0
for w in product('0123456', repeat=5):
	s = ''.join(w)
	if s.count('6') == 1:
		if '00' not in s and '11' not in s and '22' not in s and '33' not in w and '44' not in s and '55' not in s and '66' not in s:
			print(s)
			k += 1
print(k)