from turtle import *
tracer(0)
left(90)
screensize(5000, 5000)
k = 100
begin_fill()
right(30)
for i in range(18):
	fd(11 * k)
	right(120)
	fd(11 * k)
	right(60)
end_fill()
canvas = getcanvas()
for x in range(-140, 140):
	for y in range(-140, 140):
		print(canvas.find_overlapping(x*k, y*k, x*k, y*k,))
done()
