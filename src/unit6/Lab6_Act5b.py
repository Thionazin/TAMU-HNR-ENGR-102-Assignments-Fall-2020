# Name: Senhe Hao
# Assignment: Lab 6 Part 5b
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Read in input
    num_list = input("List the numbers you want to find the largest of with a space in between.").split(" ")
    largest = num_list[0]
    # Checks to see if there is a larger number, if there is that becomes the new largest
    for i in range(1, len(num_list)):
        if num_list[i] > largest:
            largest = num_list[i]
    print("The largest number is", largest)


# If file is run call main
if __name__ == "__main__":
    main()
