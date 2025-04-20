ADULT_AGE = 18  # Adult age in the US

def is_adult(age):
    """Returns True if age is 18 or above, otherwise returns False."""
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

main()
