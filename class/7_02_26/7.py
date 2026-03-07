from itertools import *
n=0
for w in product(sorted('сумка'),repeat=5):
    n+=1
    s=''.join(w)
    if s=='кумас':
        print(n)