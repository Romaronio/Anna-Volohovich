f = open(r'5.txt')
k = 0
for s in f:
	povt = []
	nepovt = []
	stroka = list(map(int, s.split()))
	for i in stroka:
		if stroka.count(i) > 1:
			povt.append(i)
		else:
			nepovt.append(i)
	if max(stroka) in nepovt and len(povt) == 3:
		k += 1
print(k)