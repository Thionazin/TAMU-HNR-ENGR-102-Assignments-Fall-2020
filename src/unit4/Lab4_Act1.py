# Name: Senhe Hao
# Assignment: Lab 4 Part 1
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do.

# Part 1a
a = 1/7
print(a)
b = a*7
print(b)

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)

from math import *
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)

# Part 1b
print(1234567891234567**2 - 1234567891234566**2)
print(1234567891234567.0**2 - 1234567891234566.0**2)
print((1234567891234567.0+1234567891234566.0) * (1234567891234567.0-1234567891234566.0))

# Part 2
# define tolerance
TOL = 1e-10
a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
# check if b and e are equal within specified tolerance
if abs(b-e) < TOL:
    print('b and e are equal within tolerance of', TOL)
else:
    print('b and e are NOT equal within tolerance of', TOL)


if abs(y-z) < TOL:
    print('y and z are equal within tolerance of', TOL)
else:
    print('y and z are NOT equal within tolerance of', TOL)

