# Name: Senhe Hao
# Assignment: Lab 6 Part 5d
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Reads in input
    print("Keep on adding lists of numbers separated by spaces to create the list that you want. To stop type \"STOP\"")
    master_list = []
    while True:
        # Adds each element in reverse order
        temp_list = input("Enter numbers").split()
        if temp_list[0] == "STOP":
            break
        temp_list = list(map(int, temp_list))
        temp_list.reverse()
        master_list.append(temp_list)
    # Sorts the reversed lists
    master_list.sort()
    # Re reverses the lists to get the actual thing
    for i in master_list:
        i.reverse()
    # Prints the result
    print(master_list)


# If file is run call main
if __name__ == "__main__":
    main()
