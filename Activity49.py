Valid = False
while not Valid:
    try:
        x = int(input("Enter an integer here: "))
        while x%2==0:
            print("Bye!")
        Valid = True
    except Exception as e:
        print("Invalid integer!") 













