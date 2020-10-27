# Name: Senhe Hao
# Assignment: Lab 9 part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


# Main function
def main():
    # Reads in file input
    input_file = open("Celsius.dat", "r", encoding="utf-8")
    input_list = input_file.readlines()
    # Conversions
    for i in range(0, input_list.__len__()):
        input_list[i] = str(round(float(input_list[i])*1.8+32, 2))+'\n'
    # Writes to file
    output_file = open("Fahrenheit.dat", "w+", encoding="utf-8")
    output_file.writelines(input_list)


# If file is run call main
if __name__ == "__main__":
    main()
