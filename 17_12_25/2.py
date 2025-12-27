from turtle import *
left(90)
k = 10
tracer(0)
screensize(5000, 5000)

for i in range(8):
    forward(22 * k)
    right(90)
    forward(33 * k)
    right(90)
pu()
backward(8 * k)
right(90)
forward(11 * k)
left(90)
pd()
for i in range(8):
    forward(73 * k)
    right(90)
    forward(62 * k)
    right(90)
pu()
for x in range(-40, 0):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(2)

update()
done()

