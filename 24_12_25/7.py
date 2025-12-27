for n in range(1000):
    s = bin(n)[2:]
    m = ''
    for i in s:
        if i == '1':
            m += '0'
        else:
            m += '1'
    s = '1' + m
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'
    s = int(s, 2)
    if s > 180:
        print(n, s)
        break



