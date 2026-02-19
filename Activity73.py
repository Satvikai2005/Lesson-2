class Rost:
    _private_message = 100

    def _prevMeth(self):
        print("You have been hacked.")
    
    def hello(self):
        print(f"This is the value of the private class variable {Rost._private_message}")

object = Rost()
object._prevMeth()
object.hello()