from turtle import *
tracer(0)
left(90)
screensize(5000, 5000)
k = 10
for i in range(6):
	fd(33 * k)
	right(90)
	fd(20 * k)
	right(90)
pu()
fd(3 * k)
right(90)
fd(9 * k)
left(90)
pd()
for i in range(6):
	fd(24 * k)
	right(90)
	fd(25 * k)
	right(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(3)
done()
