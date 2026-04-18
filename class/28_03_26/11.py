f=[0]*300000
g=[0]*300000
q=[0]*300000
for n in range(300000):
    if n<43:
        f[n]=g[n+4]
    if n >=43:
        f[n]=2*f[n-2]-f[n-4]+2
    if n<11240:
        g[n]=g[n+3]+2
    if n>=11240:
        g[n]=q[n]
    if n<21:
        q[n]=n+4
    if n>=21:
        q[n]=q[n-4]+2
print(f[2026])