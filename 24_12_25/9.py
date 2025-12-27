for n in range(1000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = s + '0'
        s = '100' + s[3:]
    else:
        s = s + '1'
        s = '111' + s[3:]
    if int(s, 2) > 128:
        print(n, s)
        break