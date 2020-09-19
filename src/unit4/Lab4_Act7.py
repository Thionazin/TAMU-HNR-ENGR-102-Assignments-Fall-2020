# Name: Senhe Hao
# Assignment: Lab 4 Part 7
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


import math


# Defines the main function
def main():
    # Reads in input
    print('Please input A.')
    a = float(input())
    print('Input B')
    b = float(input())
    print('Input C')
    c = float(input())

    # Checks if A is zero
    if a == 0:
        print('Not a quadratic, so answer is:', (-c)/b)
    else:
        # Finds the discriminant
        discriminant = b*b-4*a*c

        # Finds the square root of the discriminant
        square = math.sqrt(abs(discriminant))

        # Checks the discriminant for the conditions
        if discriminant > 0:
            print((-b + square)/(2 * a), ' and ', (-b - square)/(2 * a))
        elif discriminant == 0:
            print(-b / (2 * a))
        else:
            print(- b / (2 * a), '+', square, 'i', ' and ', - b / (2 * a), '-', square, 'i')


# If file is run, call main
if __name__ == '__main__':
    main()
