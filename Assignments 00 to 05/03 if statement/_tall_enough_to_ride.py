while True:
    height = input("How tall are you? (Press enter to stop): ")

    if height == "":
        print("Goodbye!")
        break  # Agar user enter daba de to loop ruk jaye

    height = int(height)  # String input ko integer mein convert karein

    if height >= 50:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")