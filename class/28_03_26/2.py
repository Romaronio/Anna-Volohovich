def f(n):
    if n==1:
        return 2
    if n>=2 and n%2==0:
        return f(n-1)
    if n>=2 and n%2==1:
        return 3*f(n-1)-2*n+5
print(f(15))