numbers_count = {}

while True:
    num = input("Enter a number (or press enter to stop): ")
    if num == "":
        break
    num = int(num)
    numbers_count[num] = numbers_count.get(num, 0) + 1

for num, count in numbers_count.items():
    print(f"{num} appears {count} times.")

     
