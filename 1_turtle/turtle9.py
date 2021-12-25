#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o9

from turtle import *
import math


def multy_conner(x, raduis):
    angle = 360 / x
    left(90 + angle / 2)
    length_ = 2 * raduis * math.sin(math.pi / x)
    for i in range(x):
        forward(length_)
        left(angle)


def new_position(increment):
    penup()
    setheading(0)
    forward(increment)
    pendown()


speed('slow')
setup(700, 700)
shape('turtle')
x = 3
radius = 30
count = 12
increment = 20

while True:
    multy_conner(x, radius)
    new_position(increment)
    x += 1
    radius += increment
    if x > count:
        break

exitonclick()
