# Name: Senhe Hao
# Assignment: Lab 4 Part 6
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Defines the function for calculation of the amount of widgets produced.
def production_amount(days):
    # Determines what day it's at to calculate widgets
    if days <= 10:
        return 10 * days
    elif days <= 60:
        return 100 + 40 * (days-10)
    elif days <= 100:
        return 100 + 2000 + (((39+(100-days)) * (days-60))/2)  # Area of a trapezoid to find area of region.


# Defines the main function
def main():
    # Reads in input
    print('Input the day you want to know the total production so far for. Days must be an integer between 0 and 100')
    day = input()
    # Verifies if input is legit then prints out the final statement.
    try:
        if int(day) < 0 or int(day) > 100:
            print('Invalid input')
        else:
            print('The amount of widgets made at day', day, 'is', production_amount(int(day)))
    except ValueError:
        print('Invalid input')


# If file is run, call main
if __name__ == '__main__':
    main()
