for n in range(1000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = s + '10'
    else:
        s = s + '01'
    if int(s, 2) > 200:
        print(n, int(s, 2))
        break

