f=open('6 (2).txt')
mas=[]
res=[]
o=[]
k=0

for s in f:
    mas.append(int(s))
for y in mas:
    if y%100==50:
        o.append(int(y))
p=max(o)
for i in range(len(mas)-2):
    if mas[i]!=mas[i+1] and mas[i+1]!=mas[i+2]:
        if [i+2]!=mas[i] and 10000<=abs(mas[i])<=99999 and 10000<=abs(mas[i+1])<=99999 and 10000<=abs(mas[i+2])<=99999:
            k=mas[i]+mas[i+1]+mas[i+2]
            if k<=p:
                res.append(k)
print(len(res), max(res))
