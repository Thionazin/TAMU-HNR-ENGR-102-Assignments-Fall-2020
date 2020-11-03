# Name: Senhe Hao
# Assignment: Lab 10 part 4
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Main function
def main():
    input_file = open("WeatherDataWindows.csv", "r")
    days = input_file.readlines()
    del days[0]


# If file is run call main
if __name__ == "__main__":
    main()
