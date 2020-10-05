# Name: Senhe Hao
# Assignment: Lab 6 Part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Reads in the input
    numbers = input("Enter in a line of numbers separated by a space.").split(" ")
    # loops through to find the intervals
    for i in range(1, numbers.__len__()):
        # sets a few trackers variables
        increasing = 0
        decreasing = 0
        total = 0
        # Loops through each interval in order to find if it's increasing or decreasing
        for j in range(i, numbers.__len__()):
            # checks to see if it's increasing or decreasing
            if int(numbers[j]) - int(numbers[j-i]) > 0:
                increasing += 1
            elif int(numbers[j]) - int(numbers[j-i]) < 0:
                decreasing += 1
            total += 1
        # prints the output
        print("For", i, "day intervals,", round((increasing/total)*100, 1), "% were increasing and", round((decreasing/total)*100, 1), "% were decreasing")


# If file is run call main
if __name__ == "__main__":
    main()
