# Name: Senhe Hao
# Assignment: Lab 6 Part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Merge sort function
def merge_sort(elements):
    # Checks if the list the instance of the function got is greater than 1.
    if len(elements) > 1:
        # Finds the mid points and divides and conquers the list.
        mid = len(elements)//2
        left = elements[:mid]
        right = elements[mid:]
        # Recursively searches through
        left = merge_sort(left)
        right = merge_sort(right)
        # New list of elements
        elements = []
        # Reorders the elements
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                elements.append(left[0])
                left.pop(0)
            else:
                elements.append(right[0])
                right.pop(0)
        for i in left:
            elements.append(i)
        for i in right:
            elements.append(i)
    # Returns the result
    return elements


# Main function
def main():
    print("Input the golfers and their scores. To stop accepting inputs, set the first round score to a negative")
    golfers = []
    # Reads in the input with a while loop.
    while True:
        first_round = int(input("Enter first round score"))
        # Checks if you are trying to terminate the loop
        if first_round < 0:
            break
        second_round = int(input("Enter second round score"))
        name = input("Enter name")
        # Adds the stuff to the list
        golfers.append([first_round + second_round, name])
    # Sorts the list
    new_list = merge_sort(golfers)
    print(new_list)
    made_the_cut = []
    didnt_make_it = []
    # Finds takes the lower half of the people and see if they make the cut
    for i in range(0, len(new_list)//2):
        made_the_cut.append(new_list[i][1])
    for i in range(len(new_list)//2, len(new_list)):
        didnt_make_it.append(new_list[i][1])
    # Prints the result
    print(made_the_cut)
    print(didnt_make_it)


# If file is run call main
if __name__ == "__main__":
    main()
