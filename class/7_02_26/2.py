from itertools import *
k=0
for w in product('пуля', repeat=6):
    s=''.join(w)
    if s.count('у')==2:
        k+=1
print(k)