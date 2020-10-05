# Name: Senhe Hao
# Assignment: Lab 6 Part 4
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Oh lord of the depths, great mathematician Newton, please grant thy apostle the power of math.
import math


# Main function
def main():
    # Reads in the input
    dimension = int(input("Input vector dimension as an integer"))
    vec_a = input("Input vector A as numbers with spaces in between. Format: x y z").split(" ")
    vec_b = input("Input vector B as numbers with spaces in between. Format: x y z").split(" ")
    # Calculates the magnitude using the formula
    sum_vec = 0
    for i in vec_a:
        sum_vec += int(i)**2
    print("Magnitude of vector A:", math.sqrt(sum_vec))
    sum_vec = 0
    for i in vec_b:
        sum_vec += int(i)**2
    print("Magnitude of vector B:", math.sqrt(sum_vec))
    # Adding the vectors using a for loop
    sum_vec = []
    for i in range(0, dimension):
        sum_vec.append(int(vec_a[i]) + int(vec_b[i]))
    print("A + B =", sum_vec)
    # Subtracting vectors using the same method
    sub_vec = []
    for i in range(0, dimension):
        sub_vec.append(int(vec_a[i]) - int(vec_b[i]))
    print("A - B =", sub_vec)
    # Doing the dor product using the dot product formula
    sum_num = 0
    for i in range(0, dimension):
        sum_num += int(vec_a[i]) * int(vec_b[i])
    print("A * B =", sum_num)


# If file is run call main
if __name__ == "__main__":
    main()
