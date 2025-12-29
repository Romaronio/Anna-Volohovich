def seven(n):
    m = ''
    while n > 0:
        m = str(n % 7) + m
        n = n // 7
    return m

for n in range(1000):
    k=''
    s=seven(n)
    if s[-1:]=='2':
        for i in s:
            if i=='0':
                k+=i
            if i=='1':
                k+='3'
            if i=='2':
                k+=i
            if i=='3':
                k+='1'
            if i=='4':
                k+=i
            if i=='5':
                k+=i
            if i=='6':
                k+=i
            if i=='7':
                k+=i
        k= '21'+k
    else:
        s= '1'+s[1:]+'36'
    r= int(s, 7)
    if r <744:
        print(n, r)