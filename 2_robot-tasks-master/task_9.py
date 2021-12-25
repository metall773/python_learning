#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o9-task-8-2

from pyrob.api import *


@task
def task_8_2():
    while True:
        if not wall_is_above():
            fill_cell()
        if wall_is_on_the_right():
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
