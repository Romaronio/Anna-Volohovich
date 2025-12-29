for n in range(1000):
    s=bin(n)[2:]
    if n%5==0:
        s= s+'11'
    else:
        t=bin(n//5)[2:]
        s= s+t
    r=int(s,2)
    if r>890:
        print(n, r)
        break