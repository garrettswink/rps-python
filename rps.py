# Module import
import random
import os

# Import variables containing ASCII art strings
from art import rock, paper, scissors

# Store art variables in a list
game_images = [rock, paper, scissors]


while True:
    # Clear the screen at the start of each round.
    os.system('clear')

    # Create a user input; Convert to integer; Store in a variable
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

    # Print the ASCII art from the game_images list at the index stored in the user_choice variable
    print(game_images[user_choice])

    # Select a random integer btwn 0-2 using the random module; Store in computer_choice module
    # Print the ASCII art from game_images list at the index stored in computer_choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Game Logic
    if user_choice >= 3 or user_choice < 0:
        print("Your input is invalid!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice == user_choice:
        print("Draw!")

    play_again = input("Do you want to play again? Type 'y' for Yes or 'n' for No.").lower()
    if play_again != 'y':
        print("Goodbye")
        break

