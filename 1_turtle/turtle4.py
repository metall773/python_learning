#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o4

from turtle import *


color('red', 'yellow')
speed('fastest')
setup(500, 500)

penup()
setposition(0, -151)
pendown()

begin_fill()
while True:
    forward(3)
    left(1)
    if abs(pos()) <= 150:
        break
end_fill()
done()
