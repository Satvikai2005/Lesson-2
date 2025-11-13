x = int(input("Enter a number here: "))
y = int(input("Enter a second number here: "))
if x>y: 
    print(f"{x} is greater than {y}.")
elif y>x:
    print(f"{y} is greater than {x}.")
else:
    print(f"{x} and {y} are equal.")