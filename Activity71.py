class vehicle:
     def __init__(self, max_speed, mileage):
          self.max_speed = max_speed
          self.mileage = mileage

values = vehicle(500, 30)
print("The max speed of the vehicle is ", values.max_speed, "km/h")
print("The mileage of the vehicle is ", values.mileage, "kmpl")