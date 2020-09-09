# Name: Senhe Hao
# Assignment: Lab 3 Act 3c
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


from math import *


# Main function
def main():
    # This part uses the mohr coloumb failure criterion to calculate and print the sheer stress applied to a material.
    print('This will calculate shear stress given normal stress, cohesion, and angle of internal friction.')
    # Next series of lines detail the inputs to be used.
    print('Input normal stress (lbs/in^2)')
    normal_stress = input()  # lbs/in^2
    print('Input cohesion (lbf/in^2)')
    cohesion = input()  # lbf/in^2
    print('input angle of internal friction (degrees)')
    angle_inter_fric = input()  # degrees
    # The final printed result
    print(
        'The sheer stress:',
        float(normal_stress) * tan(radians(int(angle_inter_fric))) + float(cohesion), 'lbf/in^2')  # lbf/in^2


# If this file is run, call main.
if __name__ == "__main__":
    main()
