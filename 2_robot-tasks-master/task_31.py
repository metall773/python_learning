#!/usr/bin/python3
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab2.html#o31-task-8-30

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        moving_down_to_the_wall()
        rigth = moving_rigth_to_the_wall()
        if wall_is_on_the_right():
            left = moving_left_to_the_wall()
        if left is False and rigth is False:
            return


def moving_down_to_the_wall():
    while True:
        if wall_is_beneath():
            break
        move_down()


def moving_left_to_the_wall():
    while True:
        if (wall_is_on_the_left() or
                not wall_is_beneath()):
            break
        move_left()
    if not wall_is_beneath():
        return True
    else:
        return False


def moving_rigth_to_the_wall():
    while True:
        if (wall_is_on_the_right() or
                not wall_is_beneath()):
            break
        move_right()
    if not wall_is_beneath():
        return True
    else:
        return False


if __name__ == '__main__':
    run_tasks()
