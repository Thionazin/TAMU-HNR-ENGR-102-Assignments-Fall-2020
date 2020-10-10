# Name: Senhe Hao
# Assignment: Lab 7 part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Main function
def main():
    # Reads in input
    strain = float(input("Enter the strain"))
    # Checks to see which zone the input belongs in. After checking then it calculates the stress based on the formula for that region.
    # If the value is not in a region it says it's undefined.
    if 0 <= strain <= 0.01:
        print("The stress is approximately", (4400*strain))
    elif 0.01 < strain <= 0.06:
        print("The stress is approximately", 44)
    elif 0.06 < strain <= 0.18:
        print("The stress is approximately", (16/0.12)*strain+36)
    elif 0.18 < strain <= 0.26:
        print("The stress is approximately", -125*strain+82.5)
    else:
        print("The stress is undefined at this strain value")


# If file is run call main
if __name__ == "__main__":
    main()
