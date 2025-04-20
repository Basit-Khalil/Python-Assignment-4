def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Perform integer division and get the remainder
    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Modulo operation to get remainder
    
    # Output the results
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
