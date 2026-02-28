f = open(r"2.txt")
k = 0
for s in f:
	stroka = list(map(int, s.split()))
	if sum(stroka) / len(stroka) < 30:
		k += 1
print(k)