class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        area = self.radius * self.radius * 3.14
        return f"The area of a circle with radius {self.radius} is {area}."
    
    def perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return f"The perimeter of the circle with radius {self.radius} is {perimeter}."

radius = int(input("Enter the radius of the circle here: "))
o = Circle(radius)

operation = input("What operation do you want to do perimeter or area (p/a) of a circle?: ")

if operation == "perimeter" or operation == "p":
    print(o.perimeter())
elif operation == "area" or operation == "a":
    print(o.area())
else:
    print("Enter a valid choice next time.")
  

 




