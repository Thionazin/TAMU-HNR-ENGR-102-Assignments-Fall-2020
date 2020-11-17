# Name: Senhe Hao
# Assignment: Lab 12 Part 1f
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Function for finding average velocity between times
def velocities(time_list, dist_list):
    vel_list = []
    # Loops through the lists and adds elements to the new one
    for i in range(1, len(time_list)):
        time_diff = time_list[i]-time_list[i-1]
        dist_diff = dist_list[i]-dist_list[i-1]
        vel_list.append(dist_diff/time_diff)
    return vel_list


# Main function
def main():
    # Creates the lists
    time_list = [1, 2, 3, 4, 5, 6, 7, 8]
    dist_list = [5, 6, 7, 8, 9, 20, 55, 100]
    print(velocities(time_list, dist_list))


# If this file is run call main
if __name__ == "__main__":
    main()
