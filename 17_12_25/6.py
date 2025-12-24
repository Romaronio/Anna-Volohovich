from turtle import *
left(90)
tracer(0)
k = 20
screensize(5000, 5000)

for i in range(5):
    forward(6 * k)
    right(90)
    forward(3 * k)
    right(90)
pu()
forward(4 * k)
right(90)
forward(2 * k)
right(90)
pd()
for i in range(8):
    forward(8 * k)
    right(90)
    forward(5 * k)
    right(90)
pu()
forward(4 * k)
right(90)
forward(2 * k)
left(90)
pd()
for i in range(4):
    forward(5 * k)
    left(90)
pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(2)
update()
done()