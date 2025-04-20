import random

NUM_ROUNDS = 5  # You can adjust the number of rounds here

def get_user_guess():
    """
    Prompts the user for a guess of 'higher' or 'lower'.
    Keeps prompting until valid input is received.
    """
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    while guess not in ['higher', 'lower']:
        guess = input("Please enter either 'higher' or 'lower': ").strip().lower()
    return guess

def play_round(round_num, score):
    """
    Plays a single round of the game.
    Returns updated score.
    """
    print(f"Round {round_num}")
    your_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)
    print(f"Your number is {your_num}")

    guess = get_user_guess()

    # Evaluate the guess
    correct = False
    if guess == "higher" and your_num > computer_num:
        correct = True
    elif guess == "lower" and your_num < computer_num:
        correct = True

    if correct:
        print(f"You were right! The computer's number was {computer_num}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_num}")
    
    print(f"Your score is now {score}\n")
    return score

def give_final_message(score):
    """
    Displays a final message based on the player's performance.
    """
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    for i in range(1, NUM_ROUNDS + 1):
        score = play_round(i, score)
    
    give_final_message(score)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
