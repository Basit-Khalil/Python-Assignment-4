
# Inventory dictionary
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "pear": 1000,
    "grape": 15
}

def num_in_stock(fruit):
    """Returns the number of a specific fruit in stock."""
    return inventory.get(fruit, 0)

def main():
    fruit = input("Enter a fruit: ").lower()
    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# Run the program
main()
