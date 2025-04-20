
def double_until_hundred() -> None:
    """Asks the user for a number, doubles it until it's 100 or greater, and prints the results."""
    curr_value: int = int(input("Enter a number: "))  # User input ko integer mai convert karna zaroori hai

    while curr_value < 100:
        curr_value *= 2  # Value ko double karna
        print(curr_value, end=" ")  # Output ko ek line mai rakhne ke liye end=" " use kiya

# Run the function
if __name__ == "__main__":
    double_until_hundred()
