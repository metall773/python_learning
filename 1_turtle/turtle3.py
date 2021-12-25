#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o3

from turtle import *


size = 200
angle = 90  # 72 fun
shape('turtle')
setup(500, 500)

for i in range(4):
    forward(size)
    left(angle)

exitonclick()
