positive_responses = ["yes", "y", "yeah", "sure"]
negative_responses = ["no", "n", "nope"]

response = input("Do you agree? ").lower()

if response in positive_responses:
    print("Awesome! You agreed.")
elif response in negative_responses:
    print("Alright, you disagreed.")
else:
    print("Hmm, I didn't understand that.")
