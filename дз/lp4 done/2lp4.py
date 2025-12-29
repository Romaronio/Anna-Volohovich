alfa='0123456789ab'
def od(y):
    s=''
    while y>0:
        f=y%11
        s= str(alfa[f])+s
        y=y//11
    return s
for x in range(1,3000):
    y= 9*11**210+8*11**150-x
    z= od(y)
    if z.count('0')==60:
        print(x)