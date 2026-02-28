f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\1.txt')
mas = []
for s in f:
	s = int(s)
	if s % 3 == 0 and s % 7 != 0 and s % 17 != 0 and s % 19 != 0 and s % 27 != 0:
		mas.append(s)

print(len(mas), max(mas))