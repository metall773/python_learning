#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o4-task-3-3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_above():
        move_up()
        return
    if not wall_is_beneath():
        move_down()
        return
    if not wall_is_on_the_left():
        move_left()
        return
    move_right()


if __name__ == '__main__':
    run_tasks()
