f=open('7 (2).txt')
mas=[]
res=[]
o=[]
for s in f:
    mas.append(int(s))
for r in mas:
    if r%10==5:
        o.append(r)
p=max(o)
for i in range(len(mas)-2):
    if len(str(mas[i]))==5 and len(str(mas[i+1]))==5 and mas[i+2]!=5 or len(str(mas[i+2]))==5 and len(str(mas[i+1]))==5 and mas[i]!=5 or len(str(mas[i+2]))==5 and len(str(mas[i]))==5 and mas[i+1]!=5:
        k=mas[i]+mas[i+1]+mas[i+2]
        if k > p:
            res.append(k)
print(len(res), max(res))