def add_three_copies(lst, data):
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Empty list
my_list = []

# User input
message = input("Enter a message to copy: ")

print("List before:", my_list)

# Calling function
add_three_copies(my_list, message)

print("List after:", my_list)