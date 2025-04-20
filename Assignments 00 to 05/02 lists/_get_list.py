# Empty list to store user input
user_list = []

while True:
    value = input("Enter a value: ")

    if value == "":  # Check if the input is empty
        break  # Exit loop

    user_list.append(value)  # Add value to list

print("Here's the list:", user_list)