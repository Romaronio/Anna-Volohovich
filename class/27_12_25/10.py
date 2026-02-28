res=[]
for n in range(1000):
    m=''
    s= bin(n)[2:]
    if n %2==0:
        for i in s:
            if i == '0':
                m = m+'1'
            else:
                m = m+'1'
    else:
        m+='1'
        for i in s[1:]:
            if i == '1':
                m = m+'00'
    m= int(m,2)
    if m < 600:
        res.append([m, n])
    print(max(res))