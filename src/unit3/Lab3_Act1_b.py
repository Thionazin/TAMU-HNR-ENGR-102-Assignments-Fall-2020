# Name: Senhe Hao
# Assignment: Lab 3 Act 1 Part b
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    print('This converts BTUs to Joules. Please enter a number in BTUs which gets converted to joules.')  # Print statement
    btus = input()  # In BTUs
    print(btus, 'BTUs is equal to', float(btus)*1055.0558526, 'Joules')  # Output print statement


# If this file is run, call main.
if __name__ == "__main__":
    main()
