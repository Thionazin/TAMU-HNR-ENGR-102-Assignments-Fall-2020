# Name: Senhe Hao
# Assignment: Lab 9 part 3
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
    E = A @ B @ C
    print(E, "\n")
    print(E.transpose(), "\n")
    print(numpy.linalg.solve(E, D))


# If file is run call main
if __name__ == "__main__":
    main()
