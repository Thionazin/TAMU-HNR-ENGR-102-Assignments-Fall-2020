# Name: Senhe Hao
# Assignment: Lab 12 Part 1b
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Function for finding least profitable facility
def least_profit(names, costs, value):
    # Sets everything to the 0th for now
    worst_name = names[0]
    worst = value[0] - costs[0]
    # Loops through the elements in the list
    for i in range(1, len(names)):
        # If statement to check if the ith position element is worse
        if value[i] - costs[i] <= worst:
            worst = value[i] - costs[i]
            worst_name = names[i]
    # Returns the result as a string
    return str(worst_name) + " with a net profitability of " + str(worst)


# Main function
def main():
    # Creates the lists
    fac_names = ["Umbrella Corp Singapore", "Tai Yong Medical Hengsha", "ACME Dynamite Production"]
    fac_costs = [1000000000, 38294236489324, 58493786832]
    fac_value = [12345434, 33242243, 1]
    print("The least profitable facility is:", least_profit(fac_names, fac_costs, fac_value))


# If this file is run call main
if __name__ == "__main__":
    main()
