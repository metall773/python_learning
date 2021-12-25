#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o18-task-8-28

from pyrob.api import *


@task
def task_8_28():
    while True:
        if (wall_is_on_the_right() or
                not wall_is_above()):
            break
        move_right()
    if wall_is_on_the_right():
        while True:
            if not wall_is_above():
                break
            move_left()
    while True:
        if wall_is_above():
            break
        move_up()
    while True:
        if wall_is_on_the_left():
            break
        move_left()


if __name__ == '__main__':
    run_tasks()
