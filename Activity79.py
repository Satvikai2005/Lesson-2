import random
class Fruits:
    def __init__(self):
        self.fruits = {'apple' : 'red', 'banana' : 'yellow', 'orange' : 'orange', 'mango' : 'yellow'}
    
    def quiz(self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))
            q = input("What colour is the "+fruit+"? ")
            if q.lower() == colour:
                print("You got it! Correct answer!")
                break
            else:
                print("Sorry wrong answer.")
                print("The colour was ", colour)
            again = int(input("Do you wnat to play again, enter 1 to play again and 0 to exit: "))
            if again == 0:
                print("Thanks for playing.")
                break
            elif again == 1:
                continue
            else:
                print("Enter a valid answer next time.")
object = Fruits()
print("Welcome this is guess the colour of the fruit game!")
object.quiz()