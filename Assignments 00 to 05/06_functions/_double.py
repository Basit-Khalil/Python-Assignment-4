def double(num):
    """Returns the double of the given number."""
    return num * 2

def main():
    num = int(input("Enter a number: "))  # User se number input lo
    print(f"Double that is {double(num)}")  # Double function call karke result print karo

# Function call
main()