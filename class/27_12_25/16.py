def seven(x):
    s=''
    while x>0:
        s=s+str(x%7)
        x=x//7
    return s[::-1]
ch=0
nch=0
x= 15*343**2031+7*49**1142+3*7**111+7**222-16809
r=seven(x)
for i in r:
    if int(i)%2==0:
        ch=ch+1
    else:
        nch=nch+1
print(ch-nch)