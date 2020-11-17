# Name: Senhe Hao
# Assignment: Lab 12 Part 1a
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import numpy as np


# Function for finding volume remaining
def remaining(length, width, height, radius):
    # Checks if the radius exceeds the bounds
    if radius*2 >= length or radius*2 >= width:
        return "Error, radius exceeds bounds."
    else:
        # Subtracts cylinder volume from the rectangle volume.
        vol_cyl = np.pi*radius*radius*height
        vol_rect = length*width*height
        return vol_rect - vol_cyl


# Main function
def main():
    print("Material remaining:", remaining(10, 10, 10, 3))


# If this file is run call main
if __name__ == "__main__":
    main()