from operator import *
mas = [int(i) for i in open('8.txt')]
res = []
okan = [i for i in mas if abs(i) % 10 == 9]
for i in range(len(mas) - 1):
	if xor(abs(mas[i]) % 10 == 9, abs(mas[i + 1]) % 10 == 9):
		if mas[i] ** 2 + mas[i + 1] ** 2 < max(okan) ** 2:
			res.append(mas[i] ** 2 + mas[i + 1] ** 2)
print(len(res), min(res))
