f = open(r"C:\Users\spiri\Desktop\егэ материалы\17 задание\2.txt")
mas = []
for s in f:
		s = int(s)
		if s % 9 != 0 and s % 11 != 0 and (s % 10 == 5 or s % 10 == 7):
			mas.append(s)
print(mas)
print(len(mas), max(mas) + min(mas))
