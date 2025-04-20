import random  # Import the random library to simulate random dice rolls

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Roll two dice (random integers between 1 and NUM_SIDES)
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total of the two dice rolls
    total: int = die1 + die2
    
    # Print out the results
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()
