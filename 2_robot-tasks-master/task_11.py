#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o11-task-8-4

from pyrob.api import *


@task
def task_8_4():
    while True:
        if (wall_is_above() and
                wall_is_beneath()):
            fill_cell()
        if wall_is_on_the_right():
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
