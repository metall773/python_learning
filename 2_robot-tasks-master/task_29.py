#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o29-task-7-7

from pyrob.api import *


@task
def task_7_7():
    i = 0
    while True:
        if cell_is_filled():
            i += 1
        else:
            i = 0
        if (wall_is_on_the_right() or i == 3):
            return
        move_right()


if __name__ == '__main__':
    run_tasks()
