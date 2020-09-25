# Name: Senhe Hao
# Assignment: Lab 5 Part 3a
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Creates a list to store output values
    number_list = []
    # Reads in the input
    print('Input an integer:')
    number = int(input())
    number_list.append(number)
    # A few variables to be defined and used
    continue_on = True
    iterations = 0
    # While loop to find the values
    while continue_on:
        # Breaks out of the loop if the number in 1
        if number == 1:
            break
        # Checks the value of the number and performs operations accordingly. Then iterates the iterations.
        if number % 2 == 0:
            number /= 2
            number_list.append(int(number))
            iterations += 1
        else:
            number = 3*number+1
            number_list.append(int(number))
            iterations += 1
    # Prints the output
    print('Sequence:', number_list)
    print('Iterations to reach 1:', iterations)


# If file is run call main
if __name__ == "__main__":
    main()
