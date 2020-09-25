# Name: Senhe Hao
# Assignment: Lab 5 Part 3c
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Offering the fresh blood of 12 orphans for the math package gods
import math


# Function to determine if an off number is a prime
def find_prime(number):
    # Finds the square that we divide up to
    divisor = math.floor(math.sqrt(number))
    # Determines if the number divides evenly to any number from 3 to its root. If yes it's not prime.
    for j in range(3, 1 + divisor, 2):
        if number % j == 0:
            return str(number) + ' is not a prime number'
    return str(number) + ' is a prime number'


# Main function
def main():
    # Starts off by saying that 2 is not prime
    print('2 is a prime number')
    for i in range(3, 101):
        # if it's even, then it's not prime.
        if i % 2 == 0:
            print(i, 'is not a prime number')
        else:
            print(find_prime(i))


# If file is run call main
if __name__ == "__main__":
    main()
