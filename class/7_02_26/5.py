from itertools import *
k=0
for w in permutations('0123456789',r=4):
    s=''.join(w)
    for x in '02468':
        for y in '02468':
            s=s.replace(x+y, '*')
    for t in '13579':
        for r in '13579':
            s=s.replace(t+r, '*')
    if '*' not in s and  s[0]!= '0':
        k+=1
print(k)

# from itertools import *
# k=0
# for w in permutations('0121212121', r=4):
#     s=''.join(w)
#     if '11' not in s and '22'not in s and s[0]!=0 and '00' not in s:
#         k+=1
# print(k)