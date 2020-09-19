# Name: Senhe Hao
# Assignment: Lab 4 Part 2a
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# The calculation function
def change(amount):
    change = amount % 25
    amount = amount // 25
    print('quarters', amount)
    amount = change % 10
    change = change // 10
    print('dimes', change)
    change = amount % 5
    amount = amount // 5
    print('nickles', amount)
    print('pennies', change)


# Defines the main function
def main():
    print('Input amount of change in cents.')
    inputs = input()
    print('For 63 cents, the coins dispersed are:')
    change(int(inputs))


# If file is run, call main
if __name__ == '__main__':
    main()