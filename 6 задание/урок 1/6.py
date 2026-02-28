from turtle import *
tracer(0)
left(90)
screensize(5000, 5000)
k = 20
for i in range(5):
	fd(6 * k)
	right(90)
	fd(3 * k)
	right(90)
pu()
fd(4 * k)
right(90)
fd(2 * k)
right(90)
pd()
for i in range(8):
	fd(8 * k)
	right(90)
	fd(5 * k)
	right(90)
pu()
fd(4 * k)
right(90)
fd(2 * k)
left(90)
pd()
for i in range(4):
	fd(5 * k)
	left(90)
pu()
for x in range(-40, 40):
	for y in range(-40, 40):
		goto(x * k, y * k)
		dot(2)
update()
done()
