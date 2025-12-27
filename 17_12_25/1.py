from turtle import *
# forward(), fd() - шаг вперед
# backward(), back(), bk() - шаг назад
# right() rt() - повернуть на право
# left() lt() - поворот влево
# goto(x, y), setpos(x, y) - передвинуться в точку
# penup(), pu() - поднять у черепахи хвост
# pendown(), pd() - опустить хвост
# dot(3, 'red') - поставить точку
#done() - завершить программу и вывести результат
# update() - обновление



left(90)
k = 10
tracer(0)
screensize(5000, 5000)

for i in range(6):
    forward(33 * k)
    right(90)
    forward(20 * k)
    right(90)
pu()
forward(3 * k)
right(90)
forward(9 * k)
left(90)
pd()
for i in range(6):
    forward(24 * k)
    right(90)
    forward(25 * k)
    right(90)
pu()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

update()
done()































