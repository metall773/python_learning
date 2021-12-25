#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o28-task-7-6

from pyrob.api import *


@task
def task_7_6():
    i = 0
    while True:
        if cell_is_filled():
            i += 1
        if (wall_is_on_the_right() or i == 5):
            return
        move_right()


if __name__ == '__main__':
    run_tasks()
