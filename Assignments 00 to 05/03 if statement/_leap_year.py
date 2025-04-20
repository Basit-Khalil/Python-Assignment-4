# User se year input lena
year = int(input("Enter a year: "))

# Leap year check conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("That's a leap year!")
else:
    print("That's not a leap year.")
