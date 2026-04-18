x=3
y=1
def fac(x,y):
    if x==1:
        return y
    else:
        y=y*x
        return fac(x-1, y)
print(fac(x,y))
