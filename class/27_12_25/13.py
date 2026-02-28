from turtle import *
tracer(0)
k=15
screensize(1000,1000)
lt(90)
for i in range(3):
    rt(45)
    fd(10*k)
    rt(45)
rt(315)
fd(10*k)
for i in range(2):
    rt(90)
    fd(10*k)
pu()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*k,y*k)
        dot(2)
update()
done()