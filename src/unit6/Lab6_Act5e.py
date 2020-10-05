# Name: Senhe Hao
# Assignment: Lab 6 Part 5c
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Main function
def main():
    # Reads input
    num_list = input("List the numbers you want to remove all duplicates from with a space in between.").split(" ")
    num_list = list(map(int, num_list))
    # Creates a set
    no_duplicates = {21}
    no_duplicates.remove(21)
    # Adds items into the set
    for i in num_list:
        no_duplicates.add(i)
    # Prints the final result in the form of a list
    final_list = []
    for i in no_duplicates:
        final_list.append(i)


# If file is run call main
if __name__ == "__main__":
    main()
