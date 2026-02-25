from turtle import *
tracer(0)
left(90)
screensize(5000, 5000)
k = 2
for i in range(4):
	fd(50 * k)
	left(90)
pu()
fd(50 * k)
left(135)
pendown()
for i in range(2):
	fd(102 * k)
	left(120)
	fd(182 * k)
	left(60)
update()
done()
