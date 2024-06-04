import random

# Define the valid options
options = ["rock", "paper", "scissors"]

# Initialize the player's score
score = 0

# Start the game loop
while True:
    # Ask the player for their choice
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Check if the player's choice is valid
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Generate a random choice for the computer
    computer_choice = random.choice(options)

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        score += 1
    else:
        print("You lose!")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Display the player's score
print("Your score:", score)