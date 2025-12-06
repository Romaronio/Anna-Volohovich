x = 36**8+6**20-12
s=''
while x:
    s=str((x%6))+s
    x//=6
print(s.count('5'))