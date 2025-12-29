def tri(n):
    m=''
    while n>0:
        m= str(n%3)+m
        n=n//3
    return m

for n in range(1000):
    s=tri(n)
    if n%3==0:
        s= '1'+s+'02'
    else:
        t=tri(((n%3)*4))
        s=s+t
    r=int(s,3)
    if r<100:
        print(n, r)