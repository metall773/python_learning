#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o6-task-5-3

from pyrob.api import *


@task
def task_5_3():
    while True:
        if wall_is_beneath():
            break
        move_right()
    while True:
        move_right()
        if not wall_is_beneath():
            break


if __name__ == '__main__':
    run_tasks()
