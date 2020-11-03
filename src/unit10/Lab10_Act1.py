# Name: Senhe Hao
# Assignment: Lab 10 part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import numpy
import matplotlib


# Main function
def main():
    # Creates a matrix
    A = numpy.array([[1, 2, 3, 4], [2, 3, 4, 5], [5, 6, 7, 8]])
    print(A, "\n")
    B = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(B, "\n")
    C = numpy.array([[1, 2, 3], [4, 5, 6]])
    print(C, "\n")
    D = numpy.array([[1], [2], [3]])
    print(D, "\n")
    # Multiply them
    E = A @ B @ C
    print(E, "\n")
    # Transposed E
    print(E.transpose(), "\n")
    # Solved Ex=D
    print(numpy.linalg.solve(E, D))


# If file is run call main
if __name__ == "__main__":
    main()
