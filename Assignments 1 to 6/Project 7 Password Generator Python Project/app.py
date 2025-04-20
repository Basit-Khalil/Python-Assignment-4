import random
import string

# Function to generate a random password
def generate_password(length):
    # All possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choice to select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function
def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        if length < 6:
            print("Password should be at least 6 characters long.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()
