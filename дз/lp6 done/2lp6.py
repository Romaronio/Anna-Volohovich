for n in range(1000):
    m=''
    s= bin(n)[2:]
    m= m+s[:1]
    for i in s[1:-1]:
        if i == '1':
            m+='0'
        else:
            m+='1'
    m= m+s[-1]
    r=int(m,2)
    r=r+n
    if n%2!=0 and r>300:
        print(n, r)
        break