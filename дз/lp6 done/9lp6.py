def ch(n):
    m = ''
    while n > 0:
        m = str(n % 4) + m
        n = n // 4
    return m

for n in range(1000):
    k=''
    s=ch(n)
    if s[1:1]=='3':
        for i in s:
            if i=='0':
                k+=i
            if i=='1':
                k+='3'
            if i=='2':
                k+=i
            if i=='3':
                k+='0'
        k= '21'+k
    else:
        s= '1'+s[1:]+'12'
    r=int(s, 4)
    if r<598:
        print(n, r)