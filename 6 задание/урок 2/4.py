from turtle import *
left(90)
tracer(0)
k = 10
screensize(5000, 5000)
for i in range(100):
	left(45)
	for i in range(8):
		fd(50 * k)
		right(45)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()