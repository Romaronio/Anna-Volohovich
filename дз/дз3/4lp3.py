x = 4*625**9-25**15+2*5**11-7
s=''
while x:
    s=str((x%5))+s
    x//=5
print(s.count('4'))