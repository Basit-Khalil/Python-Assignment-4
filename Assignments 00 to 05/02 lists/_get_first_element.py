def get_first_element(lst):
    print("First element:", lst[0])

# Empty list to store user input
user_list = []

# Asking user for list elements
n = int(input("Enter number of elements in the list: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

# Calling function
get_first_element(user_list)