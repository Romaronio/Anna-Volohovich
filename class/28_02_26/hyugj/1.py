f = open('1.txt')
for s in f:
    st= list(map(int, s.split()))
    print(st)