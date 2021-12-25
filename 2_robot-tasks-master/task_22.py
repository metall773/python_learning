#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o22-task-5-10

from pyrob.api import *


@task
def task_5_10():
    while True:
        while True:
            fill_cell()
            if wall_is_on_the_right():
                break
            move_right()
        if not wall_is_beneath():
            move_down()
        else:
            while True:
                if wall_is_on_the_left():
                    break
                move_left()
            return
        while True:
            fill_cell()
            if wall_is_on_the_left():
                break
            move_left()
        if not wall_is_beneath():
            move_down()
        else:
            return


if __name__ == '__main__':
    run_tasks()
