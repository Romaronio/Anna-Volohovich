f= open('9_28755.ods')
for i in f:
    g= list(map(int, i.split()))
    if max