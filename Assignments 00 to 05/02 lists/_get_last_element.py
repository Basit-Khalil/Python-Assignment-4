
def get_last_element(lst):
    print("Last element:", lst[-1])  # Accessing last element using negative indexing

# Empty list to store user input
user_list = []

# Asking user for list elements
n = int(input("Enter number of elements in the list: "))

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

# Calling function
get_last_element(user_list)
