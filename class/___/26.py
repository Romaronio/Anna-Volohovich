from turtle import *
k = 20
tracer(0)
screensize(5000, 5000)
left(90)
rt(90)
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
for x in range(-40, 40):
    for y in range(-40, 40):
        if x==0 or y==0:
            goto(x*k, y*k)
            dot(3, 'red')
        else:
            goto(x*k, y*k)
            dot(2)
update()
done()
# 178