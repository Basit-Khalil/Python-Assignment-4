# Mad Libs: A Fun Story Generator
# This Python project allows the user to fill in the blanks and create a hilarious, personalized story.

print("🎉 Welcome to the Mad Libs Game! 🎉")
print("Let's create a fun and wacky story. You'll be asked to provide different types of words, and then we'll use them to generate a hilarious tale!\n")

# User input prompts
name = input("Enter a name: ")
place = input("Enter a place: ")
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb (action word): ")
food = input("Enter a type of food: ")
emotion = input("Enter an emotion: ")
exclamation = input("Enter an exclamation (e.g., Wow, Yikes, OMG): ")

# Creating the story using f-strings
mad_lib = f"""
Once upon a time, {name} decided to go on an adventure to {place}.
Along the way, {name} encountered a very {adj1} {noun1}.
It {verb1} and made a strange sound, leaving {name} completely confused.

But then, out of nowhere, {name} found a delicious plate of {food}.
Feeling {emotion}, {name} couldn't resist and ate the whole thing.

As they finished, they shouted, "{exclamation}!" and laughed about how strange the day had turned out.
It was a truly unforgettable adventure.
"""

# Output the completed story
print("\n--- Here's your Mad Libs story ---")
print(mad_lib)

