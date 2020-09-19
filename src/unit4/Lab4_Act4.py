# Name: Senhe Hao
# Assignment: Lab 4 Part 4
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Defines the main function
def main():
    # Reads in the three numbers
    print('Type in three numbers. ex: \'1 2 3\'')
    input_list = input().split(' ')
    # Set current largest to the element at the beginning
    largest_number = int(input_list[0])
    # For loop that traverses the list, checking to see if there are any larger numbers as it goes
    for i in range(1, 3):
        if int(input_list[i]) > largest_number:
            largest_number = int(input_list[i])
    print(largest_number)


# If file is run, call main
if __name__ == '__main__':
    main()
