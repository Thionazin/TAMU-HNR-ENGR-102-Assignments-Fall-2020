# Name: Senhe Hao
# Assignment: Lab1B Part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.


# Sacrifices infants to summon the mighty power of the math package
from math import *


# This part prints my student information.
name = 'Senhe Hao'  # My Name
uin = '830004623'  # UIN
section = '236'  # Section Number
print(name, uin, section + '\n')

# This part prints an interesting line about myself.
interesting_fact = 'I can play the trumpet.'  # Fact
print(interesting_fact, '\n')

# This part prints out the results of putting these two values through ohms law.
resistance = 20  # Ohms
current = 5  # Amperes
print('Voltage of a conductor with a resistance of 20ohms and current of 5 amps:', resistance * current, 'V', '\n')  # Volts

# This part calculates and prints the kinetic energy of an object of 100kg 21m/s.
mass = 100  # kg
velocity = 21  # m/s
print('Kinetic energy of an object with a mass of 100kg and a velocity of 21m/s:', (1/2)*mass*pow(velocity, 2), 'J', '\n')  # Joules

# This part calculates and prints the Reynolds number a fluid with the velocity of 100m/s and a kinematic viscosity of 1.2 (m^2)/s and with characteristic linear dimension 2.5 m
velocity = 100  # m/s
kinematic_viscosity = 1.2  # (m^2)/s
char_lin_dimen = 2.5  # m
print('The Reynolds number for a fluid with velocity of 100m/s and a kinematic viscosity of 1.2 (m^2)/s and with characteristic linear dimension 2.5 m:', (velocity*char_lin_dimen)/kinematic_viscosity, '\n')

# This part calculates and prints the production of a well after 20 days using the Arps equation with an initial production rate of 100 barrels/day an initial decline rate of 2 barrels/day and a hyperbolic constant of 0.8.
days = 20  # Days
init_prod_rate = 100  # Barrels a day
init_decline_rate = 2  # Barrels a day
hyperbolic_constant = 0.8  # No unit
print('The final production rate of a well after 20 days with an initial production rate of 100 barrels a day and an initial decline rate of 2 barrels a day and hyperbolic constant of 0.8:', (init_prod_rate)/(pow(1 + (hyperbolic_constant*init_decline_rate*days),(1/hyperbolic_constant))), 'Units of barrels per day at day 20\n')  # Units of barrels/day @ day 20

# This part uses the mohr coloumb failure criterion to calculate and print the sheer stress applied to a material when a normal stress of 20 lbf/in^2 is applied to a material with cohesion of 2 lbf/in^2 and an angle of internal friction of 35 degrees.
normal_stress = 20  # lbs/in^2
cohesion = 2  # lbf/in^2
angle_inter_fric = 35
print('The sheer stress when a normal stress of 20lbs/in^2 is applied to a material with cohesion of 2 lbf/in^2 and an angle of internal friction of 35 degrees is:', normal_stress*tan(radians(angle_inter_fric))+cohesion, 'lbf/in^2') # lbf/in^2
