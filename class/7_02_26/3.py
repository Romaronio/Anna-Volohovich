from itertools import *
k=0
n=0
for w in product(sorted('мужчина'), repeat=6):
    s = ''.join(w)
    k+=1
    if s[0]!='ж' and s.count('ч')<=1 and k%2==0:
        n+=1
print(n)