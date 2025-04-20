import random

DONE_LIKELIHOOD = 0.3  # 30% chance of stopping

def done():
    """Randomly decides if we should stop counting."""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Counts from 1 to 10, but randomly stops if done() returns True."""
    for i in range(1, 11):
        if done():
            return  # Stop counting
        print(i)

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

# Running the main function
main()