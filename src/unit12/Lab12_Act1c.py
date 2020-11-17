# Name: Senhe Hao
# Assignment: Lab 12 Part 1c
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Function for printing the label
def label(name, city, state, zip_code, adr_line_1, adr_line_2):
    # Prints everything
    print(name)
    # Checks if there is a second line of address
    if adr_line_2 == "":
        print(adr_line_1)
    else:
        print(adr_line_1, adr_line_2)
    print(city, state, zip_code)


# Main function
def main():
    # input
    name = input("Enter name:")
    city = input("Enter city:")
    state = input("Enter state:")
    zip_code = input("Enter zip code:")
    adr_line_1 = input("Enter line 1 of your address:")
    adr_line_2 = input("Enter line 2 of address (optional, press enter if you don't have one):")
    label(name, city, state, zip_code, adr_line_1, adr_line_2)


# If this file is run call main
if __name__ == "__main__":
    main()
