from turtle import *
left(90)
tracer(0)
k = 10
screensize(5000, 5000)

for i in range(3):
	fd(2 * k)
	right(90)
	fd(3 * k)
	left(90)
right(180)
fd(6 * k)
right(90)
fd(9 * k)
pu()
back(3 * k)
right(90)
for i in range(2):
	fd(1 * k)
	right(90)
	fd(2 * k)
	left(90)
right(180)
fd(3 * k)
right(90)
fd(4 * k)
right(90)
fd(1 * k)

pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
done()