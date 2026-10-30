from turtle import *
left(90)
tracer(False)
screensize(5000,5000)
m = 10
for i in range(2):
    forward(13*m)
    right(90)
    forward(20*m)
    right(90)
up()
forward(8*m)
right(90)
back(3*m)
left(90)
down()
for i in range(2):
    forward(16*m)
    right(90)
    forward(8*m)
    right(90)
up()
for x in range(0,6):
    for y in range(8,14):
        goto(x*m, y*m)
        dot(3,"red")
print(21*14+9*17-6*6)

update()
done()
