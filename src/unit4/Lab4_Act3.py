# Name: Senhe Hao
# Assignment: Lab 4 Part 3
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Function for determining if the boolean is true or false
def parse_input(input_string):
    # Determines if true
    if input_string == 'T' or input_string == 't' or input_string == 'True':
        return True
    # Determines if false
    if input_string == 'F' or input_string == 'f' or input_string == 'False':
        return False


# Defines the main function
def main():
    # Reads in input three times for the booleans of a, b and c
    print('Enter the boolean for a')
    input_string = input()
    a_boolean = parse_input(input_string)
    print('Enter the boolean for b')
    input_string = input()
    b_boolean = parse_input(input_string)
    print('Enter the boolean for c')
    input_string = input()
    c_boolean = parse_input(input_string)

    # Print statements for the evaluations of part B
    print('a and b and c', a_boolean & b_boolean & c_boolean)
    print('a or b or c', a_boolean | b_boolean | c_boolean)

    # Part C
    # Assigning variables
    a = True
    b = False
    c = False
    # Doing stuff with the variables
    print('Xor of a and b where a is false and b is true', a ^ b)
    print('Only evaluates to true if an odd number are true', (a == True and b == c) or (b == True and a == c) or (c == True and a == b))


# If file is run, call main
if __name__ == '__main__':
    main()
