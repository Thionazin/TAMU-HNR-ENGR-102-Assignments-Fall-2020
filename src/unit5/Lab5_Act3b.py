# Name: Senhe Hao
# Assignment: Lab 5 Part 3b
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Reads in input
    input_value = (int(input('Input a positive integer')))
    # Defines the output values
    output_1 = 0
    output_2 = 1
    # For loop to find the values
    for i in range(1, input_value+1):
        output_1 += i
        output_2 *= i
    # Printing the output
    print(output_1)
    print(output_2)
    # Defines the output again
    output_1_2 = 0
    output_2_2 = 1
    # Defines the iterator
    i = 1
    # While loop to find the values
    while i <= input_value:
        output_1_2 += i
        output_2_2 *= i
        i += 1
    # The output
    print(output_1_2)
    print(output_2_2)


# If file is run call main
if __name__ == "__main__":
    main()
