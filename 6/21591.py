from turtle import *
screensize(5000, 5000)
tracer(False)
m = 10

left(90)
right(270)
for i in range(2):
    forward(8*m)
    right(120)
right(120)
for i in range(2):
    right(120)
    forward(3*m)
    right(240)
right(240)
for i in range(2):
    forward(14*m)
    right(120)
up()

for x in range(-30, 30):
    for y in range(0, 15):
        goto(x*m, y*m)
        dot(3, "red")
update()
done()
print(12*14/2)