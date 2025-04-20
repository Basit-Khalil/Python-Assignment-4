MAX_LENGTH = 3  # Define the max length for the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last element
        print("Removed:", removed_item)  # Print removed element

# Example usage
def main():
    lst = input("Enter list elements separated by space: ").split()
    print("Original list:", lst)
    shorten(lst)
    print("Final list:", lst)

main()
