from turtle import *
left(90)
k = 3
tracer(0)
screensize(5000, 5000)

for i in range(4):
    forward(50 * k)
    left(90)
pu()
fd(50 * k)
left(135)
pd()
for i in range(2):
    forward(102 * k)
    left(120)
    forward(182 * k)
    left(60)

pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(2)

update()
done()