f = open(r"C:\Users\spiri\Desktop\егэ материалы\17 задание\5.txt")
mas = [int(s) for s in f]
res = []
for i in range(len(mas) - 1):
	x, y = mas[i], mas[i + 1]
	if x * y > 0 and (x + y) % 7 == 0:
		res.append(x * y)
print(len(res), min(res))