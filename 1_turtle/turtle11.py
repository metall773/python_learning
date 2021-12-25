#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o11

from turtle import *
import math


def circle_(x, raduis, direction):
    angle = 360 / x
    length_ = 2 * raduis * math.sin(math.pi / x)
    for i in range(x):
        forward(length_)
        if direction:
            left(angle)
        else:
            right(angle)
    print(x, raduis, pos(), angle, length_)


speed('fastest')
setup(700, 700)
shape('turtle')
x = 1
radius = 40
count = 10
left(90)

while True:
    circle_(25, radius, True)
    circle_(25, radius, False)
    radius += 10
    x += 1
    if x > count:
        break

exitonclick()
