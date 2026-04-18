from itertools import *
k=0
s=[''.join(x) for x in product('аелпрь', repeat=6)]
for i in s:
    k+=1
    if i.count('л')>=2 and i[0]!='ь' and i[0]!='р':
        if k%2==0:
            print(k,i)