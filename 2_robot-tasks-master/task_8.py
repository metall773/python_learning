#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o8-task-5-7

from pyrob.api import *


@task
def task_5_7():
    while True:
        move_right()
        if not (wall_is_beneath() or
                wall_is_above()):
            break


if __name__ == '__main__':
    run_tasks()
