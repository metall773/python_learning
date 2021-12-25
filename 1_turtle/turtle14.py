#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o14

from turtle import *
import math


def Xstar(x, radius):
    angle = 360 / x
    length_ = radius / (x * 1.5) + 2 * radius * math.sin(math.pi / x)
    next_conner = x // 2

    # звезда с четным кол-вом вершин
    if (x % 2) == 0:
        start_pos_x = round(xcor())
        start_pos_y = round(ycor())
        next_conner -= 1
        angle_to_next_vertex = angle * next_conner
        while True:
            forward(2 * radius)
            right(angle_to_next_vertex)
            current_pos_x = round(xcor())
            current_pos_y = round(ycor())
            if (start_pos_x == current_pos_x and
                    start_pos_y == current_pos_y):
                break

        # если кол-во вершин не кратно четрыем
        # то сдвигаем перо на сл вершину
        if (x % 4) != 0:
            new_position(xcor(), ycor() - length_, heading())
            for i in range(x // 2):
                forward(2 * radius)
                left(angle_to_next_vertex)

    # звезда с нечетным кол-вом вершин
    else:
        angle_to_next_vertex = angle * next_conner
        for i in range(x):
            forward(2 * radius)
            right(angle_to_next_vertex)


def new_position(x, y, head=0):
    penup()
    setheading(head)
    setposition(x, y)
    pendown()


radius = 100
# speed ('fastest')
shape('turtle')
setup(radius * 8, radius * 4)

new_position(-radius * 2, radius // 2)
Xstar(6, radius)

new_position(radius, radius // 2)
Xstar(14, radius)

exitonclick()
