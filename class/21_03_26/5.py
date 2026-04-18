x=input('vvedite slovo')
y=x
def r(x):
    if len(x)<=1:
        return x
    else:
        return r(x[1:])+x[0]
print(r(x))
