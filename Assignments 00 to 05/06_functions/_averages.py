def find_average(num1, num2):
    """Do numbers ka average return karega."""
    return (num1 + num2) / 2

# User se input lena
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Function call karke average print karna
average = find_average(num1, num2)
print(f"The average of {num1} and {num2} is: {average}")