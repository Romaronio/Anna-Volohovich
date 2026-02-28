from turtle import *
x=31
k=10
tracer(0)
screensize(1000, 1000)
lt(90)
for i in range(4):
    fd(x*k)
    rt(90)
    fd(48*k)
    rt(90)
pu()
fd(27*k)
rt(90)
fd(24*k)
lt(90)
pd()
for i in range(4):
    fd(29*k)
    rt(90)
    bk(18*k)
    rt(90)
pu()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*k,y*k)
        dot(2)
update()
done()
# otvet-31