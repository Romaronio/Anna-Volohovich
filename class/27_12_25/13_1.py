from math import *
p= 960*1024
n= 16384
i= log2(n)
v= (p*i*400)/(2**23)
print(v)