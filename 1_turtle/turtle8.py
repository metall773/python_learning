#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o8

from turtle import *


# speed ('fastest')
setup(400, 400)
shape('turtle')
x = 5

while True:
    x += 5
    forward(x)
    left(90)
    if x > 200:
        break

exitonclick()
