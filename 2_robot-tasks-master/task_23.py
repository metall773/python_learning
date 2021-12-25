#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o23-task-6-6

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while True:
        if not wall_is_above():
            while True:
                if wall_is_above():
                    break
                move_up()
            while True:
                if wall_is_beneath():
                    break
                fill_cell()
                move_down()
        if not wall_is_on_the_right():
            move_right()
        else:
            while True:
                move_left()
                if not wall_is_beneath():
                    break
            return


if __name__ == '__main__':
    run_tasks()
