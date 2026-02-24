from abc import ABC, abstractmethod
class Abstractmethod:
    def i(self, x):
        print(x)
    @abstractmethod
    def t(self):
        print("I am an abstract method of the base class.")
class Childclass(Abstractmethod):
    def t(self):
        print("This is a abstract method of the child class.")

o = Childclass()
o.t()
o.i(9)