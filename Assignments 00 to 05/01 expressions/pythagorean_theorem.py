import math  # Import the math library to use the sqrt function

def main():
    # Get the two perpendicular side lengths from the user and convert them to float
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)

    # Output the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()
