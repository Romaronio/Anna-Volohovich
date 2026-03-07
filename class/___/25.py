from turtle import *
k = 20

screensize(5000, 5000)
left(90)
for i in range(100):
    fd(10*k)
    rt(48)
pu()
for x in range(-40,40):
    for y in range(-40,40):
        if x==0 and y==0:
            dot(3,'red')
        else:
            dot(2, 'white')
update()
done()
# 15