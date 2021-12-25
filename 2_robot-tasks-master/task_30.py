#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o30-task-9-3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    size = x = y = 0
    while True:
        y += 1
        while True:
            x += 1
            if wall_is_on_the_right():
                size = x
                if x != y and x + y - size != 1:
                    fill_cell()
                break
            if x != y and x + y - size != 1:
                fill_cell()
            move_right()
        if wall_is_beneath():
            while True:
                if wall_is_on_the_left():
                    break
                move_left()
            break
        move_down()
        y += 1
        while True:
            if x != y and x + y - size != 1:
                fill_cell()
            x -= 1
            if wall_is_on_the_left():
                break
            move_left()
        if wall_is_beneath():
            break
        move_down()


if __name__ == '__main__':
    run_tasks()
