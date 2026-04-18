def f(n):
    if n==1:
        return 3
    if n>1:
        return 7*f(n-1)-n+4
print(f(5))