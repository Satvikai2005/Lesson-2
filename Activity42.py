def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter choice(1/2/3/4): "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == 1:
    print("The result is:", add(num1, num2))
elif choice == 2:
    print("The result is:", subtract(num1, num2))
elif choice == 3:
    print("The result is:", multiply(num1, num2))
else:
    print("The result is:", divide(num1, num2))













