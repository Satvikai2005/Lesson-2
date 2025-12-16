import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(500,500)
x = turtle.Turtle()
number_of_sides = 9
length_of_sides = 80
angle = 360/number_of_sides
for i in range(number_of_sides):
    x.forward(length_of_sides)
    x.right(angle)
turtle.done()











