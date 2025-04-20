
def get_user_data():
    """Asks user for first name, last name, and email, then returns them as a tuple."""
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email  # Returns a tuple

def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)

# Run the program
main()
