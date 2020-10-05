# Name: Senhe Hao
# Assignment: Lab 6 Part 5a
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Main function
def main():
    # Read input
    num_list = input("List the numbers you want to multiply with a space in between.").split(" ")
    multi = 1
    # Iterates through and multiplies everything
    for i in num_list:
        multi *= int(i)
    print("Multiplying everything in there gets us", multi)

# If file is run call main
if __name__ == "__main__":
    main()
