import random
attempts = 0
print("Welcome! This is the guss the number game.")
print("I am thinking a number between 1 and 100.")
number_guess = random.randint(1,100)
while True:
    user_number_guess = input("Take a guess:")
    try:
        user_number_guess = int(user_number_guess)
    except ValueError:
        print("Enter an integer please.")
        continue
    attempts += 1
    if attempts >= 6:
        print("You have reached you limit of guessing the number.")
        break
    if number_guess==user_number_guess:
        print(f"Congratulations! You guessed it right. The number was {number_guess}.")
        break
    elif user_number_guess <= 100 and user_number_guess >= 1:
        if user_number_guess > number_guess:
            print("Your guess is higher than my chossen number. Try again.")
        if user_number_guess < number_guess:
          print("Your guess is lower than my chossen number. Try again.")
    else:
        print("No that was not the number I was thinking. Try again")
        continue