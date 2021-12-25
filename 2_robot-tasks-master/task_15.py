#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o15-task-8-21

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        while True:
            move_down()
            if wall_is_beneath():
                break
    else:
        while True:
            move_up()
            if wall_is_above():
                break
    if wall_is_on_the_left():
        while True:
            move_right()
            if wall_is_on_the_right():
                break
    else:
        while True:
            move_left()
            if wall_is_on_the_left():
                break


if __name__ == '__main__':
    run_tasks()
