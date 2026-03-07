f=open('4 (2).txt')
mas=[]
res=[]
for s in f:
    mas.append(int(s))
for i in range(len(mas)-2):
    if mas[i]>0 or mas[i+1]>0 or mas[i+2]>0:
        res.append(mas[i]+mas[i+1]+mas[i+2])
print(len(res), min(res))