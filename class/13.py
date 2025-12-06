# 1 sposob
# stroka = 'aaabcadfaabmpq'
# s= stroka.split('a')
# x = max(s, key=len)
# print(x, len(x))

2 sposob
k=0
res=0
stroka = 'aaabcadfaabmpq'
s= stroka.split('a')
s = set(s)
for x in s:
    for y in x:
        k+=1
    if k>res:
        res=k
    k=0
print(res)