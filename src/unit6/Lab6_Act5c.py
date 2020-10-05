# Name: Senhe Hao
# Assignment: Lab 6 Part 5c
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Reads input
    num_list = input("List the numbers you want to find the second smallest of of with a space in between.").split(" ")
    num_list = list(map(int, num_list))
    # Sorts elements
    num_list.sort()
    # Finds the second smallest
    if len(num_list) > 1:
        print("The second smallest element is", num_list[1])


# If file is run call main
if __name__ == "__main__":
    main()
