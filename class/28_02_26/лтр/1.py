f=open("1 (2).txt")
mas=[]
res=[]
k=0
for s in f:
    s=int(s)
    mas.append(s)
for i in range(len(mas)):
    if mas[i]%11==0 and mas[i+1]%11==0:
        k+=1
        res.append(mas[i]+mas[i+1])
print(k, min(res))
