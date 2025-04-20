
# Maximum value for Fibonacci sequence
MAX_VALUE = 10000

# First two terms of Fibonacci sequence
a, b = 0, 1

# Print Fibonacci sequence until the terms are less than MAX_VALUE
while a < MAX_VALUE:
    print(a, end=" ")  # Print the term
    a, b = b, a + b  # Move to the next term
