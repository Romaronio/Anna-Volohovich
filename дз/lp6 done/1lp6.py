for n in range(1000):
    s= bin(n)[2:]
    if s.count('1')%2==0:
        s= '100' + s[3:]+ '0'
    else:
        s= '111'+s[3:]+'1'
    s= int(s,2)
    if s>128:
        print(n, s)
        break
