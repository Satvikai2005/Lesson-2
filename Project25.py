#asking user to enter a number
number = int(input("Enter a number here:"))
odd = [x for x in range(1, number+1) if x % 2 != 0]
print(f"The list of odd numbers until {number} is {odd}")


#making a list of fruits
fruits = ["banana", "apple", "mango", "orange"]
#converting the first letter of the fruits capital
capital_first_letters = [i.capitalize() for i in fruits]
print(f"This is the list of fruits with the first lettr capital:{capital_first_letters}")

