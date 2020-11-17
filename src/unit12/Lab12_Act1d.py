# Name: Senhe Hao
# Assignment: Lab 12 Part 1d
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import os


# Function for changing the csv
def reformat(name):
    # Opens input and reads everything into a list
    input_file = open(name, "r")
    entries = input_file.readlines()
    input_file.close()
    # Loops through the read elements as strings in a list and replaces all , with \t
    for i in range(0, len(entries)):
        entries[i] = entries[i].replace(",", "\t")
    # Gets the name of the file by splitting the .csv off
    temp = name.split(".")
    output_file = open(temp[0]+".tsv", "w+")
    # Writes everything
    output_file.writelines(entries)
    output_file.close()


# Main function
def main():
    name = input("Enter csv name:")
    reformat(name)


# If this file is run call main
if __name__ == "__main__":
    main()
