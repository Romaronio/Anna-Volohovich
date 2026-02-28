from operator import *
mas = [int(i) for i in open('9.txt')]
okan = [i for i in mas if i % 100 == 12]
res = []
for i in range(len(mas) - 1):
	if xor(mas[i] in okan, mas[i + 1] in okan):
		if (mas[i] + mas[i + 1]) ** 2 < max(okan) ** 2:
			res.append(mas[i] + mas[i + 1])
print(len(res), max(res))
