for n in range(1000):
    s = bin(n)[2:]
    if n % 5 == 0:
        r=s+'11'
    else:
        r= s+ str(bin(n//5)[2:])
    if int(r,2) > 896:
        print(n, r)
        break
