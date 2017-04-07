sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snikers", "M&Ms", "Twizzkers"]

while True:
    choice = input("Would you like a SODA, some CHIPS, or a Candy? ").lower()
    try:
        if choice == "sodas":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("Sorry, I didn't undestand that.")
            continue
    except IndexError:
        print("We're all out of {}! Sorry".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
