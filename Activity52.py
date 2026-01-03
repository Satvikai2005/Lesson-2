#square root calculation
import math
def calculate_square_root(number):
    return math.sqrt(number)

#finding the factorial of a number
import math 
def calculate_factorial(number):
    return math.factorial(number)

number = int(input("Enter a number here:"))
choice = input("Whta do you want to do of the number? Find square root or factorial?")
if choice == "factorial":
    result = calculate_factorial(number)
    print(result)
else:
    result = calculate_square_root(number)
    print(result)
