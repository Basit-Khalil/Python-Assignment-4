
def greet(name):
    """Prints a greeting message with the given name."""
    print(f"Greetings {name}!")

def main():
    """Gets user input and calls the greet function."""
    name = input("What's your name? ")
    greet(name)

main()
