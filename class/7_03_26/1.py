from turtle import *
left(90)
screensize(1000, 1000)
k=10
tracer(0)
for i in range(6):
    fd(33*k)
    rt(90)
    fd(20*k)
    rt(90)
pu()
fd(3*k)
rt(90)
fd(9*k)
lt(90)
pd()
for i in range(6):
    fd(24*k)
    rt(90)
    fd(25*k)
    rt(90)
pu()
for x in range(-40, 40):
    for y in range (-40, 40):
        goto(x*k,y*k)
        dot(2)
done()
