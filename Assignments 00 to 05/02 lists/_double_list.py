def double_numbers(numbers):
    return [num * 2 for num in numbers]

def main():
    numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print(f"The doubled numbers are: {double_numbers(numbers)}")

if __name__ == "__main__":
    main()
