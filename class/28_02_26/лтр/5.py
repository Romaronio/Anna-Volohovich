f=open('5 (2).txt')
mas=[]
res=[]
for s in f:
    mas.append(int(s))
for i in range(len(mas)-1):
    for t in range(1000):
        if  mas[i]**0.5==t or mas[i+1]**0.5==t:
            res.append(mas[i]+mas[i+1])
print(len(res), max(res))