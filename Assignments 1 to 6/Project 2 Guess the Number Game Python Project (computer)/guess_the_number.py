import random

def guess_the_number():
    # The computer picks a random number between 1 and 10
    number_to_guess = random.randint(1, 10)
    attempts = 0
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    while True:
        # User input
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < 1 or user_guess > 10:
                print("Please guess a number between 1 and 10.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
