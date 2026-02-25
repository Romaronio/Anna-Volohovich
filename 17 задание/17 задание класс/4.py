f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\4.txt')
mas = [int(s) for s in f]
res = []
for i in range(len(mas) - 1):
	x, y = mas[i], mas[i + 1]
	if (x + y) % 3 == 0 and (x + y) % 6 != 0 and abs((x * y)) % 10 == 8:
		res.append(x + y)
print(len(res), max(res))