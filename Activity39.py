import turtle
turtle.Screen().bgcolor("Silver")
turtle.Screen().setup(300,300)
x = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        x.forward(size+1)
        x.left(90)
        size -= 5
    size += 1
turtle.done()














