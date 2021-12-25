#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o7

from turtle import *


# speed ('fastest')
setup(400, 400)
shape('turtle')
x = 1

while True:
    x += 1 / 11
    forward(int(x))
    left(15)
    if x > 30:
        break

exitonclick()
