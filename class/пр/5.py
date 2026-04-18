for n in range(999):
    s=bin(n)[2:]
    r= s.count('1')
    s=s+str(r%2)
    t= s.count('1')
    s=s+str(t%2)
    if int(s, 2)>253:
        print(n, int(s,2))
        break
