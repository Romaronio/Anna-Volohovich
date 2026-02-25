from operator import xor
res = []
mas = [int(i) for i in open(r'6.txt')]
deli = len([i for i in mas if i % 5 == 0])
for i in range(len(mas)-1):
	if xor(mas[i] < 0, mas[i + 1] < 0):
		if mas[i] + mas[i + 1] < deli:
			res.append(mas[i] + mas[i + 1])
print(len(res), max(res))