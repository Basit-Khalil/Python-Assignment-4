import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        else:
            return "You lose!"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "You win!"
        else:
            return "You lose!"

# Function to start the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
play_game()
