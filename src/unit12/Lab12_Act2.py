# Name: Senhe Hao
# Assignment: Lab 12 Part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import turtle
import math


# Function for drawing tallies
def tally_maker(amount):
    """Draws tallies with given parameters"""
    tally = turtle.Turtle()
    # Checks how many full rows and also has the remainders
    remainder = int(amount) % 25
    times = int(amount) // 25
    # Keeps track of the y position
    y = 0
    # First for loop in order to draw the rows of full 25
    for j in range(0, times):
        # Keeps track of current x position
        x = 0
        for i in range(1, 26):
            # Adds a diagonal on every 5
            if i % 5 == 0:
                # Draws a slant
                tally.right(135)
                tally.forward(30 * math.sqrt(2))
                tally.right(225)
            else:
                # Draws a line
                tally.penup()
                tally.goto(x * 10, y)
                tally.pendown()
                tally.goto(x * 10, y+30)
            # iterates the x position
            x += 1
        # Moves everything down
        y -= 50
    x = 0
    # Second for loop for the individuals
    for i in range(1, remainder+1):
        if i % 5 == 0:
            tally.right(135)
            tally.forward(30 * math.sqrt(2))
            tally.right(225)
        else:
            tally.penup()
            tally.goto(x * 10, y)
            tally.pendown()
            tally.goto(x * 10, y+30)
        x += 1
    turtle.done()


# Main function
def main():
    """main function"""
    # input for tallies
    amount = input("How many tallies?")
    # makes sure it isn't graphing negative tallies
    if int(amount) < 0:
        return
    # calls the function
    tally_maker(int(amount))


# If this file is run call main
if __name__ == "__main__":
    main()
