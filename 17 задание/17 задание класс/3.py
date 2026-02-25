f = open(r'C:\Users\spiri\Desktop\егэ материалы\17 задание\3.txt')
mas = []
for s in f:
	s = int(s)
	print(hex(s))
	if hex(s)[-1] == 'b' and s % 7 == 0 and s % 6 != 0 and s % 13 != 0 and s % 19 != 0:
		mas.append(s)
print(sum(mas), len(mas))