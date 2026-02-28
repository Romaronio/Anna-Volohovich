from turtle import *
left(90)
tracer(0)
k = 10
screensize(5000, 5000)
right(198)
for i in range(5):
	fd(10 * k)
	left(144)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()