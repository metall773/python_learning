#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o26-task-2-4

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    for y in range(5):
        for x in range(9):
            cross()
            move_right(4)
        cross()
        move_left(36)
        if y != 4:
            move_down(4)


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
