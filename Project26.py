class Dog():
  animal = "dog"
  def __init__ (self, breed, colour):
    self.breed = breed
    self.colour = colour

def display_details(self):
  print(f"Details: {self.colour.capitalize()} {self.breed.capatalize()} {self.animal}")

dog1 = Dog("labrador", "brown")
dog2 = Dog("golden retriever", "gold")

print("Dog1:")
dog1.display_details()
print("\nDog2:")
dog2.display_details()
