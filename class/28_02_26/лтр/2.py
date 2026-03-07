f=open('2 (2).txt')
mas=[]
res=[]
for s in f:
    mas.append(int(s))
for i in range(len(mas)-1):
    if mas[i]>1234 or mas[i+1]>1234:
        res.append(mas[i]**2+mas[i+1]**2)
print(len(res), max(res))

