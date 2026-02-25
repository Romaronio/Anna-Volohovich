f = open(r'6.txt')
k = []
for s in f:
	s = list(map(int, s.split()))
	povt = [ i for i in s if s.count(i) == 3 ]
	nepovt = [ i for i in s if s.count(i) == 1 ]
	if len(povt) == 3 and len(nepovt) == 4 and sum(nepovt) / 4 <= povt[0]:
			print(sum(s))
