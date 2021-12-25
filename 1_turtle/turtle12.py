#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o12

from turtle import *
import math


def arc(x, raduis, extent):
    angle = 360 / x
    length_ = 2 * raduis * math.sin(math.pi / x)
    for i in range(int(x / (360 / extent)) + 1):
        forward(length_)
        right(angle)


x = 1
radius = 50
count = 9
speed('fastest')
setup(radius * 2 * count, radius * 6)
shape('turtle')


# self implemented arc
penup()
setposition(-(radius - count / 2) * count, radius)
pendown()
while True:
    setheading(90)
    arc(40, radius, 180)
    setheading(270)
    arc(40, radius / 6, 180)
    x += 1
    if x > count:
        break

# by system ACR
x = 1
penup()
setposition(-(radius - count / 2) * count, -radius)
pendown()
setheading(270)
while True:
    circle(radius, -180)
    circle(radius / 6, -180)
    x += 1
    if x > count:
        break

exitonclick()
