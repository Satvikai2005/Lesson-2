class Circle:
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    area = self.radius*self.radius*3.14
    return f"The are of a circle with radius {radius} is {area}."
  def perimeter(self):
    perimeter = 2*3.14*self.radius
    return f"The perimeter of the circle with radius {radius} is {perimeter}"
radius = int(input("Enter the radius of the circle here: "))
o = 
operation = input("What operation do you want to do perimeter of area (p/a) of a circle?: ")
if operation == "perimeter" or operation == "p":
   print(perimeter())
elif operation == "area" or operation == "a":
   print(area())
else:
   print("Enter a valid choice next time.")

  

 



