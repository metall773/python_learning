#!/usr/bin/python3

import matplotlib.pyplot as plt
# import matplotlib.patches as patches


def Circle(radius):
    circle = plt.Circle(
        (0,
         0),
        radius,
        facecolor='red',
        edgecolor='blue',
        linestyle='dotted',
        linewidth='2.2')
    plt.gca().add_patch(circle)
    plt.plot()
    # plt.axis('axis')
    plt.title('Circle')
    plt.grid()
    plt.show()


def main():
    radius = float(input('Enter the radius:'))
    Circle(float(radius))


main()
