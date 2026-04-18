def f(n):
    if n==1:
        return 1
    if n>=2:
        return f(n-1)+ g(n-1)+n**2
def g(n):
    if n==1:
        return 1
    if n>=2:
        return f(n-1)+g(n-1)*4
print(f(20)//g(15))