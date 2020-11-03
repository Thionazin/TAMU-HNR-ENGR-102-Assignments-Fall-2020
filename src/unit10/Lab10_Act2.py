# Name: Senhe Hao
# Assignment: Lab 10 part 2
# Class: ENGR102-236
# An aggie does not lie, cheat, nor steal, nor tolerate those who do


import numpy
import matplotlib
import matplotlib.pyplot as plt
import math


# Main function
def main():
    # Plot 1
    plt.plot([2, 5, 1, 7, 324, 46, 12])
    # labels
    plt.ylabel('Completely Random Numbers')
    plt.xlabel('Completely Random x values')
    plt.legend(['line'])
    plt.title('Plot 1')
    # show plot
    plt.show()
    # Plot 2
    # arange the values
    x = numpy.arange(0., 10., 0.5)
    plt.plot(x, x**20+8, 'b^')
    # adds labels
    plt.legend(['blue triangles'])
    plt.title('Plot 2')
    plt.xlabel('Some x values')
    plt.ylabel('Some y labels')
    # shows the plot
    plt.show()
    # Plot 3
    # creates some data
    data = {'a': numpy.arange(50),
            'c': numpy.random.randint(0, 50, 50),
            'd': numpy.arange(50)}
    data['b'] = data['a'] * 100 + 4828 + numpy.random.randn(50)
    # creates the plot
    plt.scatter('a', 'b', c='c', s='d', data=data)
    # adds labels
    plt.title('Is this a line or what?')
    plt.xlabel('I think this is x idk')
    plt.ylabel('hmmmmmmmmmm')
    plt.legend(['some sort of color'])
    # show plot
    plt.show()
    # Plot 4
    # data sets
    categories = ['one', 'two', 'three', 'four']
    values = ['5', '10', '15', '20']
    # labels
    plt.ylabel('amount')
    plt.xlabel('value')
    plt.suptitle('You can see 4 categories')
    # creates the plot
    plt.bar(categories, values)
    # show plot
    plt.show()
    # Plot 5
    # creates data
    one = numpy.arange(0.0, 2.0, 0.1)
    # determines the plot
    plt.figure()
    # subplot 1
    plt.subplot(211)
    plt.plot(one, one**2+one*5+10, 'ro')
    # subplot 2
    plt.subplot(212)
    plt.plot(one, one**2-one**3+one*3, 'bo')
    # show the plot
    plt.show()
    # Plot 6
    # data
    random = numpy.random.randn(50)
    plt.hist(random, 10)
    # labels
    plt.title('A histogram')
    plt.ylabel('Something idk')
    plt.xlabel('Arbitrary x values')
    plt.legend(['blue'])
    # show the plot
    plt.show()
    # Plot 7
    # data
    z = numpy.linspace(4, 16, 32)
    x = z**2
    y = z * 20
    # labels
    plt.figure().gca(projection='3d').plot(x, y, z)
    plt.title('a line in 3d')
    plt.legend(['blue line'])
    # show plot
    plt.show()
    # Plot 8
    # data
    u = numpy.linspace(-2, 2, 200)
    v = numpy.linspace(0, 2 * numpy.pi, 60)
    [u, v] = numpy.meshgrid(u, v)
    a = 1
    b = 1
    c = 1
    x = a * numpy.cosh(u) * numpy.cos(v)
    y = b * numpy.cosh(u) * numpy.sin(v)
    z = c * numpy.sinh(u)
    # plot
    plt.figure().gca(projection='3d').plot_surface(x, y, z)
    # showing plot
    plt.show()

# If file is run call main
if __name__ == "__main__":
    main()
