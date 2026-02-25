def five(x):
	s = ''
	while x:
		s = str(x % 5) + s
		x //= 5
	return s

for x in range(1, 55):
	for y in range(1, 50):
		s = five(5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x)
		if int(s, 5) > 0 and s.count('0') == 10:
			print(x * y)