import random

def print_random_numbers() -> None:
    """Prints 10 random numbers in the range 1 to 100."""
    for _ in range(10):
        print(random.randint(1, 100), end=" ")  # Random number print karega

    print()  # Newline for better formatting

# Run the function
if __name__ == "__main__":
    print_random_numbers()
