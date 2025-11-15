bmi = None
height = int(input("Enter your height in m: "))
weight = int(input("nter your weight in kg: "))
if bmi<18.5:
    print("Your under weight.")
elif bmi<24.9:
    print("Your healthy.")
elif bmi<29.9:
    print("Your fat.")
else:
    print("Obesity.")