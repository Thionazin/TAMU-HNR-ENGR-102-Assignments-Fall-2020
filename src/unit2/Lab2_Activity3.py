# Name: Senhe Hao
# Assignment: Lab 2 Activity 3
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Function for determining the distance from the start regardless of how much time passes
def distance_from(value):
    # returns the distance traveled by using linear interpolation and modulus operations with the circumference.
    return (50 + ((565 / 15) * (value-30))) % 3141.59265358979  # Seconds


# Function for linear interpolating the distance from the start between t=30 to t=45
def interpolate(value):
    # Returns the
    return 50 + ((565 / 15) * (value-30))  # Meters


# Defines main function
def main():
    # Sets desired t to 37
    time = 37  # Seconds
    # Calls function to interpolate the distance from the start.
    print(interpolate(time), 'm')
    # Sets desired t to 1200
    time = 1200  # Seconds
    # Calls function to interpolate regardless of time.
    print(distance_from(time), 'm')


# If this file is the one that is run, call the main method.
if __name__ == "__main__":
    # Calls main method.
    main()
