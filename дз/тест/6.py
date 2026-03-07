def free(n):
    s=''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s[::-1]

for n in range(1, 1000):
    t=free(n)
    if n%3==0:
        r=t+t[-2:]
    else:
        p= (t.count('1')+t.count('2')*2)*3
        r=t+free(p)
    if int(r) > 208 and r[-1]==1:
            print(int(r,3))
            break
