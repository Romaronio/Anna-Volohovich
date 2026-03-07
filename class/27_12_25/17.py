def seven(y):
    s=''
    while y>0:
        s=str(y%7)+s
        y=y//7
    return s
for x in range(1,2300):
    y= 7**350+7**150-x
    z=seven(y)
    if z.count('0')==200
        print(x)