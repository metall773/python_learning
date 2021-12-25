#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o17-task-8-27

from pyrob.api import *


@task
def task_8_27():
    while True:
        move_up()
        if cell_is_filled():
            break
    move_right()
    if cell_is_filled():
        return
    else:
        move_left()
        move_left()


if __name__ == '__main__':
    run_tasks()
