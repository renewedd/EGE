from turtle import *
tracer(False)
m = 15
screensize(5000, 5000)
left(90)

for i in range(2):
    forward(10*m)
    right(90)
    forward(20*m)
    right(90)
up()
forward(3*m)
right(90)
forward(7*m)
left(90)
down()
for i in range(2):
    forward(70*m)
    right(90)
    forward(90*m)
    right(90)

up()
for x in range(7,21):
    for y in range(3,11):
        goto(x*m, y*m)
        dot("3","red")
print((21-7)*(11-3))

update()
done()

