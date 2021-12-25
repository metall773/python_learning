#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o21-task-4-11

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for y in range(13):
        for x in range(y):
            fill_cell()
            move_right()
        fill_cell()
        for x in range(y):
            move_left()
        move_down()


if __name__ == '__main__':
    run_tasks()
