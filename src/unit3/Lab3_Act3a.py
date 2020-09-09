# Name: Senhe Hao
# Assignment: Lab 3 Act 3a
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # This part prints out the results of putting these two values through ohms law.
    print('This calculates voltage given resistance and current.')
    # Input 1
    print('Please enter resistance (ohms)')
    resistance = input()  # Ohms
    # Input 2
    print('Please enter current (A)')
    current = input()  # Amperes
    # Calculation
    print('Voltage:', float(resistance) * float(current), 'V')  # Volts


# If this file is run, call main.
if __name__ == "__main__":
    main()
