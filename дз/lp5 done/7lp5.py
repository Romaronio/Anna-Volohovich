from math import *
p= 1920*1080
n= 65536
i= log2(n)
v= (p*i*100)/(2**13)
k= (4*(2**20))/v
o= (4*(2**20))-(v*10)
print(o)