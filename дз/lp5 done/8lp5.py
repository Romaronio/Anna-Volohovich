r=[]
p= 800*540
i= 7
v= (p*i)/(2**10)

p2= 640*500
i2= 50
v2= (p2*i2)/(2**10)

p3= 1100*800
i3= 3
v3= (p3*i3)/(2**10)

p4= 430*240
i4= 14
v4= (p4*i4)/(2**10)

s= 200
t= v/s
r.append(t)
t2= v2/s
r.append(t2)
t3 = v3/s
r.append(t3)
t4= v4/s
r.append(t4)
m= max(r)
print(m)
# otvet - 79