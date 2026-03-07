x = 7**15 + 2*7**12 - 7**13 - 21
s=''
while x:
    s= str((x%7))+s
    x//=7
z = set(s)
print(len(z))
