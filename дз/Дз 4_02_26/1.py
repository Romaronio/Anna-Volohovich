f=open(r'1.txt')
k=0
for s in f:
    m= [int(i) for i in s.split()]
    # if max(m)< m[0]+m[1]+m[2]+m[3]-max(m) and:
    m.sort()
    print(m)