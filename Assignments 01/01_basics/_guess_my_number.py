
import random

def guess_my_number() -> None:
    """User guesses a randomly generated number between 0 and 99."""
    secret_number: int = random.randint(0, 99)  # Random number generate karega
    guess: int = -1  # Initial value jo range mai nahi hai

    print("I am thinking of a number between 0 and 99...")

    while guess != secret_number:
        guess = int(input("Enter a guess: "))  # User ka input lein

        if guess < secret_number:
            print("Your guess is too low\n")
        elif guess > secret_number:
            print("Your guess is too high\n")

    print(f"Congrats! The number was: {secret_number}")

# Run the game
if __name__ == "__main__":
    guess_my_number()
