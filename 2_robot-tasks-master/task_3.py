#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o3-task-3-1

from pyrob.api import *


@task
def task_3_1():
    while True:
        move_right()
        if wall_is_on_the_right():
            break


if __name__ == '__main__':
    run_tasks()
