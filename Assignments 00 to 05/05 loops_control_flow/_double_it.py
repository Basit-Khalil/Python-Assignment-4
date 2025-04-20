# User se input lena
curr_value = int(input("Enter a number: "))

# Jab tak curr_value 100 se chhoti hai, tab tak double karna
while curr_value < 100:
    curr_value *= 2  # Number ko double karna
    print(curr_value, end=" ")  # Same line me print karna