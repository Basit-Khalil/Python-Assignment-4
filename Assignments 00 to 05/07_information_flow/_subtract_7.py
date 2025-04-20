def subtract_seven(num):
    """Subtracts 7 from num and returns the result."""
    return num - 7

def main():
    number = int(input("Enter a number: "))  # User input le raha hai
    result = subtract_seven(number)  # Function call ho raha hai
    print("Result after subtracting 7:", result)  # Output print kar raha hai

# Run the program
main()