# Name: Senhe Hao
# Assignment: Lab1B Part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# function for interpolation. dx, dy, and dz are the changes for the respective properties. xc, yc, and zc are the initial values at each location.
def multiple_interpolation(dx, dy, dz, xc, yc, zc, time, time_init):
    # Returns what is calculated. The change is multiplied by the time and has the initial 'C' value added.
    return 'time of interest = ' + str(time + time_init) + ' seconds\n' + 'x0 = ' + str(
        dx * time + xc) + ' m\n' + 'y0 = ' + str(dy * time + yc) + ' m\n' + 'z0 = ' + str(dz * time + zc) + ' m' + '\n' \
            '---------------------'


# Defines main function
def main():
    change_x = (22 / 71)  # m/s
    change_y = (-8 / 71)  # m/s
    change_z = (3 / 71)  # m/s
    init_x = 1  # m
    init_y = 3  # m
    init_z = 7  # m
    initial_time = 13  # seconds
    iter_value = 20  # seconds
    iter_max = 50  # seconds
    iter_number = (iter_max - iter_value) / 4  # interval in seconds
    # While loop that terminates when iter_value passes 50
    while(iter_value <= iter_max):
        # Prints the interpolation using the variables defined above
        print(multiple_interpolation(change_x, change_y, change_z, init_x, init_y, init_z, iter_value - initial_time,
                                     initial_time))
        # iter_value is increased by 7.5
        iter_value += iter_number


# If this is run, call main.
if __name__ == "__main__":
    main()
