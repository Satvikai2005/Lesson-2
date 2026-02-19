class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"The value of x is {self.x} and the value of y is {self.y}.")

object = Point(49, 58)
print((object))