from turtle import *
left(90)
k = 10
tracer(0)
screensize(5000, 5000)

for i in range(8):
    forward(16 * k)
    right(90)
    forward(22 * k)
    right(90)
pu()
forward(5 * k)
right(90)
forward(5 * k)
left(90)
pd()
for i in range(8):
    forward(52 * k)
    right(90)
    forward(77 * k)
    right(90)
pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(2)

update()
done()



