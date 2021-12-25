#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o25-task-2-2

from pyrob.api import *


@task
def task_2_2():
    move_down()
    for i in range(4):
        cross()
        move_right(4)
    cross()


def cross():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()
