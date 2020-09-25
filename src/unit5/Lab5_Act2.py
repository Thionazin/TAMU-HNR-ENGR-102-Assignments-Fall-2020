# Name: Senhe Hao
# Assignment: Lab 5 Part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Variable to keep track of the approximation value
    approx = 3
    # Variable to keep track of the stuff that gets divided
    track = 2
    # Prints the 3
    print(approx)
    # A for loop that prints out the next 15 approximations
    for i in range(0, 14):
        # Checks if the next element needs to be added or subtracted from approx
        if i % 2 == 0:
            # Calculates the approximation and iterates the track value
            approx += (4/(track*(track+1)*(track+2)))
            print(approx)
            track += 2
        else:
            approx -= (4/(track*(track+1)*(track+2)))
            print(approx)
            track += 2


# If file is run call main
if __name__ == "__main__":
    main()
