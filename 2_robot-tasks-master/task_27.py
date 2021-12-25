#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o27-task-7-5

from os import rename
from pyrob.api import *


@task
def task_7_5():
    x = -1
    while True:
        for i in range(x):
            if wall_is_on_the_right():
                return
            move_right()
        x += 1
        if not wall_is_on_the_right():
            move_right()
        if not wall_is_on_the_right():
            fill_cell()


if __name__ == '__main__':
    run_tasks()
