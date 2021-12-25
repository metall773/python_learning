#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o6

from turtle import *


radius = 150
# speed ('fastest')
setup(400, 400)
shape('turtle')

for i in range(12):
    right(30)
    forward(radius)
    stamp()
    right(180)
    forward(radius)
    right(180)

exitonclick()
