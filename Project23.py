try:
    user_input = int(input("Enter a number: "))
    odd_numbers_under = [i for i in range(user_input) if i % 2 != 0]

    another_odd_list = [i for i in range(user_input, user_input + 20) if i % 2 != 0]
    
    print(f"Odd numbers under {user_input}: {odd_numbers_under}")
    print(f"Another list of odd numbers: {another_odd_list}")
except ValueError:
    print("Please enter a valid integer.")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

updated_fruits = [fruit.capitalize() for fruit in fruits]

print(updated_fruits)