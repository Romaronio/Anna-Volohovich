alfa='0123456789abcdefghijklmnopq'
def ds(y):
    s=''
    while y>0:
        f= y%27
        s= str(alfa[f])+s
        y= y//27
    return s
for x in range(1,7290):
    y= 27**298+27**269-x
    z=ds(y)
    print(z.count('0'))