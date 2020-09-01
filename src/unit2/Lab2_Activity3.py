# Name: Senhe Hao
# Assignment: Lab1B Part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.

import math


def distance_from(value):
    return (50 + ((565 / 15) * (value-30))) % 3141.59265358979


def interpolate(value):
    return 50 + ((565 / 15) * (value-30))


def main():
    time = 37
    print(interpolate(time), 'm')
    time = 1200
    print(distance_from(time), 'm')


if __name__ == "__main__":
    main()
