mas = [int(i) for i in open('7.txt')]
res = []
deli = len([i for i in mas if i % 3 == 0])
for i in range(len(mas) - 1):
	if (mas[i] < 0 or mas[i + 1] < 0) and ((mas[i] + mas[i + 1]) < deli):
			res.append(mas[i] + mas[i + 1])
print(len(res), max(res))