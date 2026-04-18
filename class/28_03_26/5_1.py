f=[0]*13000
g=[0]*13000
for n in range(13000):
    f[n]=3*(g[n-2]+5)
    if n<8:
        g[n]=3*n
    if n>=8:
        g[n]= g[n-3]+2
print(f[12345])