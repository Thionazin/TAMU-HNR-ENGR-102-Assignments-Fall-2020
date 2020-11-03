# Name: Senhe Hao
# Assignment: Lab 10 part 3
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Main function
def main():
    # generates the arrays
    v = np.array([1, 0])
    M = np.array([[1.0058, -0.087156], [0.087156, 1.00583]])
    # iterator value
    x = 1
    # lists of values
    x_values = [1]
    y_values = [0]
    # while loop to multiply
    while x < 180:
        print(M @ v)
        v = M @ v
        x += 1
        x_values.append(v[0])
        y_values.append(v[1])
    # creates the final plot
    plt.plot(x_values, y_values)
    # labels
    plt.ylabel('Y values')
    plt.xlabel('X values')
    plt.title('Plot of Mv=v where m then gets multiplied by the new point. Looks like a swirl.')
    # showing plot
    plt.show()


# If file is run call main
if __name__ == "__main__":
    main()
