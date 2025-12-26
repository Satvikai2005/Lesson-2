def shutdown():
    # Prompting user for input
    user_input = input("Do you want to shut down the system? (Yes/No): ")

    # Checking the conditions
    if user_input.lower() == "yes":
        print("Shutting down")
    elif user_input.lower() == "no":
        print("Not shutting down")
    else:
        print("Please select an option")

# Calling the function
shutdown()


