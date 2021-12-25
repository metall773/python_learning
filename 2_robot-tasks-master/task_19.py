#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o19-task-8-29

from pyrob.api import *


@task
def task_8_29():
    while True:
        if wall_is_on_the_left():
            break
        move_left()
    if wall_is_above():
        while True:
            if wall_is_on_the_right():
                break
            move_right()
    if wall_is_above():
        return
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
