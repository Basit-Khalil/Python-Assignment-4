# Constants
PROMPT: str = "What do you want? "
JOKE: str = """Here is a joke for you!
Panaversity GPT - Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12.
Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies:
'because they had eggs'"""
SORRY: str = "Sorry I only tell jokes"

def joke_bot() -> None:
    """Asks the user what they want and tells a joke if they ask for it."""
    user_input: str = input(PROMPT).strip()  # Strip removes extra spaces

    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

# Run the joke bot
if __name__ == "__main__":
    joke_bot()

     