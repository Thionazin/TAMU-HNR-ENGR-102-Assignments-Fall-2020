# Name: Senhe Hao
# Assignment: Lab 3 Act 1 Part d
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    print('This converts Seconds per revolution to Hertz. Please enter a number in s/r which gets converted to Hz.')  # Print statement
    sec_rev = input()  # In Seconds per revolution
    print(sec_rev, 'Seconds per revolution is equal to', (1/float(sec_rev)), 'Hertz')  # Output print statement


# If this file is run, call main.
if __name__ == "__main__":
    main()
