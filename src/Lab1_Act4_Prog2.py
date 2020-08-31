# Name: Senhe Hao
# Assignment: Lab1B Part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.

# Imports the math
from math import *

# Shows what the function is
print('This shows the evaluation of function 1 𝑓(𝑥) = sin(x)/x evaluated close to x = 0')

# My guess
print('I\'m guessing 1 because I\'ve done a problem on this equation before')

# Uses a for loop in order to print 8 different evaluations of the function.
temp = 1
for i in range(0, 8):
    print('f(', temp, ') =', sin(temp)/temp)
    temp /= 10
print()

# Shows function 2
print('This shows the evaluation for function 2 𝑔(𝑥) = (1 - cos(x))/(x)^2 evaluated close to x = 0')

# My guess
print('I\'m guessing 0.5 because it\'s never going to be greater than 1 and x^2 will make it equal to 0.5')

# Uses a for loop to evaluate function 2 at 8 spots
temp = 1
for i in range(0, 8):
    print('𝑔(', temp, ') =', (1 - cos(temp))/pow(temp, 2))
    temp /= 10
print()

# Shows function 3
print('This shows the evaluation of function 3 ℎ(𝑥) = (1 + (1/x))^x evaluated close to x = infinity')

# My guess
print('I\'m guessing 2.7 because this is the function for e.')

# Uses a for loop to evaluate function 3 at 8 spots
temp = 1
for i in range(0, 8):
    print('ℎ(', temp, ') =', pow((1 + (1 / temp)), temp))
    temp *= 10
print()
