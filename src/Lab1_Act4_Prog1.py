# Name: Senhe Hao
# Assignment: Lab1B Part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.

# Imports the math
from math import *

# This line prints an interesting line about myself.
print('I can play the trumpet.', '\n')

# This line prints out the results of putting these two values through ohms law.
print('Voltage of a conductor with a resistance of 20ohms and current of 5 amps:', 20*5, 'V', '\n')

# This line calculates and prints the kinetic energy of an object of 100kg 21m/s.
print('Kinetic energy of an object with a mass of 100kg and a velocity of 21m/s:', (1/2)*100*pow(21, 2), 'J', '\n')

# This line calculates and prints the Reynolds number a fluid with the velocity of 100m/s and a kinematic viscosity of 1.2 (m^2)/s and with characteristic linear dimension 2.5 m
print('The Reynolds number for a fluid with velocity of 100m/s and a kinematic viscosity of 1.2 (m^2)/s and with characteristic linear dimension 2.5 m:', (100*2.5)/1.2, '\n')

# This line calculates and prints the production of a well after 20 days using the Arps equation with an initial production rate of 100 barrels/day an initial decline rate of 2 barrels/day and a hyperbolic constant of 0.8.
print('The final production rate of a well after 20 days with an initial production rate of 100 barrels a day and an initial decline rate of 2 barrels a day and hyperbolic constant of 0.8:', (100)/(pow(1 + (0.8*2*20),(1/0.8))), 'Units of barrels per day at day 20\n')

# This line uses the mohr coloumb failure criterion to calculate and print the sheer stress applied to a material when a normal stress of 20 lbf/in^2 is applied to a material with cohesion of 2 lbf/in^2 and an angle of internal friction of 35 degrees.
print('The sheer stress when a normal stress of 20lbs/in^2 is applied to a material with cohesion of 2 lbf/in^2 and an angle of internal friction of 35 degrees is:', 20*tan(radians(35))+2, 'lbf/in^2')