import random
print("Welcome! This is the guss the number game.")
print("I am thinking a number between 1 and 10.")
number_guess = random.randint(1,10)
while True:
    user_number_guess = input("Take a guess:")
    try:
        user_number_guess = int(user_number_guess)
    except ValueError:
        print("Enter an integer please.")
        continue
    if number_guess==user_number_guess:
        print(f"Congratulations! You guessed it right. The number was {number_guess}.")
        break
    else:
        print("No that was not the number I was thinking. Try again")
        continue













