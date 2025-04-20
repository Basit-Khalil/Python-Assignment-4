def sum_numbers(numbers):
    return sum(numbers)

def main():
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print(f"The sum of the numbers is: {sum_numbers(numbers)}")

if __name__ == "__main__":
    main()