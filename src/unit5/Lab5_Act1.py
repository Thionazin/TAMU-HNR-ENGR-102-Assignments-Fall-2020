# Name: Senhe Hao
# Assignment: Lab 5 Part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


def main():
    # Reads in the input
    a = int(input("Input A"))
    b = int(input("Input B"))
    c = int(input("Input C"))
    d = int(input("Input D"))
    lower = float(input("Lower Bound"))
    upper = float(input("Upper Bound"))
    # Computes the y lowers and uppers
    y_lower = (a * (lower**3)) + (b * (lower**2)) + (c * lower) + d
    y_upper = (a * (upper**3)) + (b * (upper**2)) + (c * upper) + d
    # x is created in order to keep track of iterations.
    x = 0
    # Hard code the tolerance
    tolerance = 1e-6
    # A while loop that terminates when the conditions are met
    while (upper - lower) >= tolerance:
        # Put p in the middle
        p = (upper + lower) / 2
        # defines f(p)
        f_p = (a * (p**3)) + (b * (p**2)) + (c * p) + d
        # iterates x per iteration
        x += 1
        # Checks the relation of lower and upper with 0
        if y_upper > 0 and y_lower < 0:
            # If the f of p is less than zero we make the lower bound the new p. Else do the opposite
            if f_p < 0:
                lower = p
            elif f_p > 0:
                upper = p
        # Basically the previous one except all reversed.
        elif y_upper < 0 and y_lower > 0:
            if f_p > 0:
                lower = p
            elif f_p < 0:
                upper = p
        # If f of p is zero we break
        if f_p == 0:
            break
    # Prints the results
    print("The root is x = %.3f" % p)
    print(x, "iterations")


if __name__ == "__main__":
    main()
