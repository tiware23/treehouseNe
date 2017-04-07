import os
# make a list to hold onto our items
shopping_list = []
# print out instructions on how to use the app

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_help():
    clear_screen()
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding itens.
Enter 'HELP' for this HELP.
Enter 'SHOW' to see your current list.
""")

def show_list():
# print out the list
clear_screen()
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def show_list_append(new_item):
    shopping_list.append(new_item)
    print("Add product {} and we got {}".format(new_item, len(shopping_list)))

show_help()

while True:
    # ask for new items
    new_item = input("> ")
    # Be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    # add new items to our list
    show_list_append(new_item)
