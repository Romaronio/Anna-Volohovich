f=[0]*3000
for n in range(3000):
    if n==1:
        f[1]=1
    if n>1:
        f[n]=n*f[n-1]
print((3*f[2025]+f[2024])/f[2023])