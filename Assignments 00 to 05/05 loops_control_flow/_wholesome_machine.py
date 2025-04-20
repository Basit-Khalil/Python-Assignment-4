# Correct affirmation
correct_affirmation = "I am capable of doing anything I put my mind to."

print("Please type the following affirmation:")
while True:
    user_input = input()  # User se input lena
    if user_input == correct_affirmation:
        print("That's right! :)")
        break  # Loop se bahar nikalna
    else:
        print("Hmmm, that was not the affirmation. Please try again:")
