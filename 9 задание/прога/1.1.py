f = open(r"1.txt")
k = 0
for s in f:
	stroka = list(map(int, s.split()))
	if len(set(stroka)) != 3:
		k += 1
print(k)