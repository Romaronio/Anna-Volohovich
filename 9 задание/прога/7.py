f = open(r'7.txt')
k = 0
for s in f:
	a = [int(x) for x in s.split()]
	a1 = sorted(a)
	if a[0] > a[1] > a[2] > a[3] > a[4] > a[5] > a[6] and ((a1[0] + a1[6]) / 2) > ((a1[1] + a1[2] + a1[3] + a1[4] + a1[5]) / 5):
		print(sum(a))
		break
		k += 1
print(k)