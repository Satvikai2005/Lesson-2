# creating the game Rock, Paper, Scissors
import random

print("Welcome! This is the rock paper scissors game.")
choicez = ["Rock", "Paper", "Scissors"]

while True:
    computer_guess = random.choice(choicez)

    user_guess = input("Choose between Rock, Paper, Scissors (r/p/s): ")

    if user_guess not in ['r', 'p', 's']:
        print("Enter a valid choice r, p, s")
        continue

    if computer_guess == "Rock" and user_guess == "r":
        print("Two rocks smash each other. It's a tie.")
    elif computer_guess == "Rock" and user_guess == "p":
        print("Paper covers rock. You win!")
    elif computer_guess == "Rock" and user_guess == "s":
        print("I win! Rock smashes scissors.")
    elif computer_guess == "Paper" and user_guess == "p":
        print("Paper and paper. It's a tie.")
    elif computer_guess == "Paper" and user_guess == "r":
        print("I win! Paper covers rock.")
    elif computer_guess == "Paper" and user_guess == "s":
        print("You win! Scissors cut paper.")
    elif computer_guess == "Scissors" and user_guess == "p":
        print("Scissors cut paper. I win!")
    elif computer_guess == "Scissors" and user_guess == "r":
        print("Rock smashes scissors. You win!")
    elif computer_guess == "Scissors" and user_guess == "s":
        print("Scissors and scissors. It's a tie.")

    playing_again = input("Do you want to play again? Yes or No? ")
    if playing_again != "Yes":
        break


