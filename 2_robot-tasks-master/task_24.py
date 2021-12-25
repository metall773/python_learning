#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o24-task-2-1

from pyrob.api import *


@task
def task_2_1():
    move_right()
    move_down()
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
