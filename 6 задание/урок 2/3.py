from turtle import *
left(90)
tracer(0)
k = 20
screensize(5000, 5000)
for i in range(7):
	fd(20 * k)
	right(240)
	fd(10 * k)
	right(240)
	fd(20 * k)
	right(120)
	fd(10 * k)
	right(120)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()