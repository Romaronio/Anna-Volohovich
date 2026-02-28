f = open(r'8.txt')
k = 0
for s in f:
	s = list(map(int, s.split()))
	povt = []
	nepovt = []
	for i in s:
		if s.count(i) > 1:
			povt.append(i)
		else:
			nepovt.append(i)
	if len(povt) == 3:
		if max(s) in nepovt:
			k += 1
print(k)