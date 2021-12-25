#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o5

from turtle import *


def draw_square(size=250, angle=90):
    for i in range(4):
        forward(size)
        left(angle)


size = 15
# speed ('fastest')
setup(400, 400)
shape('turtle')

for i in range(15):
    new_position = (i * size) - 3 * size / 4
    penup()
    setposition(-new_position, -new_position)
    pendown()
    draw_square(i * size * 2)

exitonclick()
