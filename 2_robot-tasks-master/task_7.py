#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o7-task-5-4

from pyrob.api import *


@task
def task_5_4():
    while True:
        if wall_is_beneath():
            break
        move_down()
    while True:
        move_right()
        if not wall_is_beneath():
            break
    move_down()
    while True:
        move_left()
        if wall_is_on_the_left():
            break


if __name__ == '__main__':
    run_tasks()
