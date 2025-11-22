print("Choose your ride:")
print("1. Car")
print("2. Bike")
choice = input("Enter 1 or 2:")
if choice == '1':
    print("You selected car.")
    print("Select what type of car: ")
    print("1. BMW")
    print("2. Audi")
    choice2 = input("Enter 1 or 2: ")
    if choice2 == '1':
        print("You have selected BMW.")
    else:
        print("You have selected Audi.")
elif choice == '2':
    print("You selected bike.")
    print("Select what type of bike: ")
    print("1. Yamaha")
    print("2. Hero")
    choice3 = input("Enter 1 or 2: ")
    if choice3 == '2':
        print("You have selected Hero.")
    else:
        print("You have selected Yamaha.")
else:
    print("Sorry, only two options.")


