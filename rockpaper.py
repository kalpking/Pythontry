import random

print("Rock, Paper, Scissors")

# the possible choices the player and the computer can make
choices = ["rock", "paper", "scissors"]

while True:
    # player choice
    player_choice = input("Your choice: ").lower()
    if player_choice not in choices:
        print("Invalid choice, try again.")
        continue

    # computer choice
    computer_choice = random.choice(choices)

    # determine the winner
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")

    # ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "no":
        break

print("Thanks for playing!")