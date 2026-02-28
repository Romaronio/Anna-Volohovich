from turtle import *
k = 20
tracer(0)
screensize(5000, 5000)
left(90)
for i in range(7):
    fd(20*k)
    rt(240)
    fd(10*k)
    rt(240)
    fd(20*k)
    rt(120)
    fd(10*k)
    rt(120)
pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(2)
update()
done()
# 76