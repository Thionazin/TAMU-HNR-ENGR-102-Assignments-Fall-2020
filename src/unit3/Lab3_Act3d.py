# Name: Senhe Hao
# Assignment: Lab 3 Act 3d
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


from math import *


# Main function
def main():
    # This part calculates and prints the production of a well.
    # Details
    print('This calculated the production of the well provided with inputs.')
    # Inputs
    print('Input how many days later')
    days = input()  # Days
    print('Input initial production rate')
    init_prod_rate = input()  # Barrels a day
    print('Input initial decline rate')
    init_decline_rate = input()  # Barrels a day
    print('Input hyperbolic constant')
    hyperbolic_constant = input()  # No unit
    # Calculation and print statement for the final answer.
    print(
        'The production rate:',
        float(init_prod_rate) / (pow(1 + (float(hyperbolic_constant) * float(init_decline_rate) * float(days)), (1 / float(hyperbolic_constant)))),
        'Units of barrels per day\n')  # Units of barrels/day


# If this file is run, call main.
if __name__ == "__main__":
    main()
