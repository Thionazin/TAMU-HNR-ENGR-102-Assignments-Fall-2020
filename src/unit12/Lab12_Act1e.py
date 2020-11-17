# Name: Senhe Hao
# Assignment: Lab 12 Part 1e
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Function for finding min, max, and mean
def min_max_mean(list1):
    # Sets everything to the 0th value for now
    mini = list1[0]
    maxi = list1[0]
    total = 0
    # Loops through to check for min, max, and add the element to the total
    for item in list1:
        if item < mini:
            mini = item
        if item > maxi:
            maxi = item
        total += item
    # Returns all 3 desires values as a tuple
    return mini, maxi, total/(list1.__len__())


# Main function
def main():
    a_list = [12, 35, 454, 56, 5, 3, 55, 3, 5, 342, 544, 6343]
    print(min_max_mean(a_list))


# If this file is run call main
if __name__ == "__main__":
    main()
