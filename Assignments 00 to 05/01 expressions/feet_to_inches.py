# Conversion factor: 12 inches in 1 foot
INCHES_IN_FOOT = 12

def main():
    feet: float = float(input("Enter number of feet: "))  # Input number of feet
    inches: float = feet * INCHES_IN_FOOT  # Convert feet to inches
    print(f"That is {inches} inches!")  # Output the result in inches

if __name__ == '__main__':
    main()
