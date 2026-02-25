f = open(r'C:\Users\spiri\Desktop\егэ материалы\9 задание\дз\10.txt')
for s in f:
	povt = [int(i) for i in s if s.count(i) > 1]