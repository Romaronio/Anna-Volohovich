x=10
def f(x):
    if x==0:
        return 0
    if x!=0:
        x= x-1
        print(x)
        return f(x)
print(f(x))
