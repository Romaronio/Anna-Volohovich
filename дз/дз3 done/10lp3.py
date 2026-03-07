x = 216**6+216**4+36**6-6**14-24
s=''
while x:
    s= str((x%6))+s
    x//=6
z = set(s)
print(len(z))
