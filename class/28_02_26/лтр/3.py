f=open('3 (2).txt')
mas=[]
res=[]
for s in f:
    mas.append(int(s))
for i in range(len(mas)-1):
    if (mas[i]*mas[i+1])%74==0:
        res.append(mas[i]+mas[i+1])
print(len(res), max(res))