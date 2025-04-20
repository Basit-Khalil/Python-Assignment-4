import random
import string

# Dictionary of words with categories (for a more advanced version)
words_dict = {
    "animals": ["elephant", "giraffe", "tiger", "kangaroo", "zebra"],
    "fruits": ["apple", "banana", "cherry", "grape", "orange"],
    "colors": ["red", "blue", "green", "yellow", "purple"]
}

# Function to get a random word from the dictionary
def get_random_word(category):
    return random.choice(words_dict[category])

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to start the game
def play_game():
    # Select a category
    print("Welcome to Hangman!")
    print("Categories: animals, fruits, colors")
    category = input("Choose a category: ").lower()

    # Check if the category is valid
    if category not in words_dict:
        print("Invalid category. Please choose from 'animals', 'fruits', or 'colors'.")
        return
    
    word = get_random_word(category)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # The number of incorrect guesses allowed

    print(f"\nYour word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        
        # Ask for user input (guess)
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        # Check if the user has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

# Start the game
play_game()
