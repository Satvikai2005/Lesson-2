def factorial(number):
    '''
    Calculating the factorial of a given number.
    '''
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}.")















