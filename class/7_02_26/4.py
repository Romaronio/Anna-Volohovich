from itertools import *
k=0
for w in product('0123456', repeat=5):
    s= ''.join(w)
    for i in '0123456':
        s=s.replace(i*2,'*')
    if s.count('6')==1 and '*' not in s and s[0]!= '0':
        k+=1
print(k)