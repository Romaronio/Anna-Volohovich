x=5
y=0
def sym(x,y):
    if x==0:
        return y
    else:
        y=y+x
        return(sym(x-1,y))
print(sym(x,y))