#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o32-task-8-18

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    ax = 0
    while True:
        if not wall_is_above():
            while True:
                if wall_is_above():
                    break
                move_up()
                if cell_is_filled():
                    ax += 1
            while True:
                if wall_is_beneath():
                    break
                fill_cell()
                move_down()
        if (wall_is_above() and
                wall_is_beneath()):
            fill_cell()
        if not wall_is_on_the_right():
            move_right()
        if (not wall_is_above() and
                not wall_is_beneath()):
            mov('ax', ax)
            return


if __name__ == '__main__':
    run_tasks()
