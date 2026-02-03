class parrot:
     species = "bird"
     def __init__(self, name, age):
          self.name = name
          self.age = age
parrot1 = parrot("Many", 8)
parrot2 = parrot("Kiwi", 6)
print(f"{parrot1.name} is a {parrot1.species}.")
print(f"{parrot2.name} is also a {parrot2.species}.")
print(f"{parrot1.name} is {parrot1.age} years old.")
print(f"{parrot2.name} is {parrot2.age} years old.")