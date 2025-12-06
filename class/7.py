alfa='0123456789abcdefghijklmnopq'
s=''
x=2*2187**2020+729**2021+2*243**2022+81**2023+2*27**2024-6561
while x>0:
    f=x%27
    s=str(alfa[f])+s
    x=x//27
alfa2 = 'abcdefghijklmnopq'
summ=0
for i in alfa2:
    summ+= s.count(i)
print(summ)
