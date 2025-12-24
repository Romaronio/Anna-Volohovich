from turtle import *
left(90)
k = 10
tracer(0)
screensize(5000, 5000)
right(30)
for i in range(18):
    forward(11 * k)
    right(120)
    forward(11 * k)
    right(60)

pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(2, 'red')

update()
done()