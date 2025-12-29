for n in range(1000):
    s=bin(n)[2:]
    if n%3==0:
        s= s+s[-3:]
    else:
        t=bin(((n%3)*3))[2:]
        s=s+t
    r=int(s,2)
    if r>=200:
        print(n, r)
        break