#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o13

from turtle import *
import math


def arc(x, raduis, extent):
    angle = 360 / x
    length_ = 2 * raduis * math.sin(math.pi / x)
    for i in range(int(x / (360 / extent)) + 1):
        forward(length_)
        right(angle)


def new_position(x, y, head=0):
    penup()
    setheading(head)
    setposition(x, y)
    pendown()


radius = 200
speed('fastest')
setup(radius * 3, radius * 3)
shape('turtle')

stamp()
new_position(0, radius)
begin_fill()
arc(40, radius, 360)
color('yellow')
end_fill()

color('black')
new_position(-radius / 2 + radius / 12, radius / 2)
color('blue')
begin_fill()
arc(20, radius / 6, 360)
end_fill()

color('black')
new_position(radius / 2 + radius / 12, radius / 2)
color('blue')
begin_fill()
arc(20, radius / 6, 360)
end_fill()

pensize(radius / 14)
color('black')
new_position(radius / 10, radius / 5, 270)
forward(radius / 3)

color('red')
pensize(radius / 14)
new_position(radius / 1.8 + radius / 7, -radius / 3, 251)
arc(40, radius / 1.6, 144)

hideturtle()

exitonclick()
