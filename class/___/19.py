from turtle import *
k = 20
tracer(0)
screensize(5000, 5000)
left(90)
for i in range(2):
    right(120)
    forward(7*k)
right(300)
for i in range(2):
    right(120)
    fd(7 * k)
pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)
update()
done()
# 42