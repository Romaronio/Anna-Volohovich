from turtle import *
left(90)
tracer(0)
k = 10
screensize(5000, 5000)
for i in range(95):
	fd(5 * k)
	right(72)
	back(5 * k)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()