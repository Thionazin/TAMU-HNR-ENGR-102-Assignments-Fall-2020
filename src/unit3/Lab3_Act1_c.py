# Name: Senhe Hao
# Assignment: Lab 3 Act 1 Part c
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    print('This converts Pascals to Millimeters of Mercury. Please enter a number in Pascals which gets converted to mmHg.')  # Print statement
    pascals = input()  # In Pascals
    print(pascals, 'Pascals is equal to', float(pascals)*0.007500638, 'mmHg')  # Output print statement


# If this file is run, call main.
if __name__ == "__main__":
    main()
