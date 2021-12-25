#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o1-task-1-1

from pyrob.api import *


@task
def task_1_1():
    move_right(2)
    move_down()


if __name__ == '__main__':
    run_tasks()
