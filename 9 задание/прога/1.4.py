f = open(r'4.txt')
l = 0
for s in f:
	stroka = list(map(int, s.split()))
	stroka.sort(reverse=True)
	if max(stroka) ** 2 > (stroka[1] * stroka[2] * stroka[3] * stroka[4] * stroka[0]) / max(stroka):
		if stroka[0] + stroka[1] > (stroka[2] + stroka[3] + stroka[4]) * 2:
			l += 1
print(l)