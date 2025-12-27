for n in range(1000):
    s = bin(n)[2:]
    s = s + str((s.count('1') % 2))
    s = s + str((s.count('1') % 2))
    if int(s, 2) > 3123:
        print(n, int(s))
        break