try:
    age = int(input("Enter your age here: "))
    if age % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError as wrong:
    print("Invalid input.")
except Exception as e:
    print(e)