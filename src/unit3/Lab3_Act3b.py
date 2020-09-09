# Name: Senhe Hao
# Assignment: Lab 3 Act 3b
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # This part prints out the results of putting these two values through the kinetic energy equation.
    print('This calculates kinetic energy given mass and velocity.')
    # Input 1
    print('Please enter mass (kg)')
    mass = input()  # kilograms
    # Input 2
    print('Please enter velocity (m/s)')
    velocity = input()  # meters/second
    # Calculation
    print('Kinetic Energy:', (1/2)*float(mass)*pow(float(velocity), 2), 'J')  # Volts


# If this file is run, call main.
if __name__ == "__main__":
    main()
