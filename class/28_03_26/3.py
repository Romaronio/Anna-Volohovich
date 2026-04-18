def f(n):
    if n<=3:
        return n
    if n>3 and n%2==0:
        return n+5*f(n-4)
    if n%2==1 and n>3:
        return 2*n+f(n-4)

r=[]
for n in range(1,220):
    if f(n) %3==0:
        r.append(n)
print(len(r))