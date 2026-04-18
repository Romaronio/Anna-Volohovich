from turtle import *
tracer(0)
k=20
screensize(1000,1000)
lt(90)
rt(315)
for i in range(8):
    fd(12*k)
    rt(45)
    fd(6*k)
    rt(135)
pu()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*k,y*k)
        dot(2,'red')
update()