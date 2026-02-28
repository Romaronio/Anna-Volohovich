for n in range(1000):
    s= bin(n)[2:]
    if n%5==0:
        s= s +'11'
    else:
        y= n//5
        s= s+ (bin(y)[2:])
    s= int(s,2)
    if s > 896 and n%2==0:
        print(n, s)
        break