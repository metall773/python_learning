#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o20-task-4-3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for y in range(6):
        for x in range(26):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        for x in range(26):
            fill_cell()
            move_left()
        fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
