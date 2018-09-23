from wheat_class import *
from potato_class import *

def display _menu():
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Please select an option from the above menu")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: ")
            if choice in (1,2):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return(choice)

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    crop = create_crop()
    manage_crop(crop)
