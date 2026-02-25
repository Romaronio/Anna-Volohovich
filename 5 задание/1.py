for n in range(1, 1000):
	s = bin(n)[2:]
	if n % 2 == 0:
		s = s + '10'
	else:
		s = s + '01'
	if int(s, 2) > 200:
		print(int(s, 2), n)
		break