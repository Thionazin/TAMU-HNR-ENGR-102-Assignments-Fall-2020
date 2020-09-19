# Name: Senhe Hao
# Assignment: Lab 4 Part 5
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Defines the main function
def main():
    # Reads in the inputs
    print('Input the characteristic velocity of the flow in m/s')
    char_vel = int(input())
    print('Input the pipe diameter in m')
    diameter = int(input())
    print('Input the fluid kinematic viscosity m^2/s')
    fluid_vis = int(input())

    reynolds_number = (char_vel * diameter) / fluid_vis

    # Check the bounds of the number to classify it
    if reynolds_number < 2300:
        print('The Reynolds number is', reynolds_number, ' which makes it laminar')
    elif reynolds_number > 2900:
        print('The Reynolds number is', reynolds_number, ' which makes it fully turbulent')
    else:
        print('The Reynolds number is', reynolds_number, ' which makes it in transition')




# If file is run, call main
if __name__ == '__main__':
    main()
