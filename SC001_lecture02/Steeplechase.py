"""
File: Steeplechase.py
Name:Jasper
---------------------------------
TODO:
"""

from karel.stanfordkarel import *

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
    # defeat
    # while front_is_clear():
    #     move()
    #     if not front_is_clear():
    #         jump()
    # pass


def jump():
    """
    pre-condition:頭朝右
    post-condition:頭朝右
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:頭朝右
    post-condition:頭朝上
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()


def cross():
    """
    pre-condition:頭朝上
    post-condition:頭朝下
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:頭朝下
    post-condition:頭朝右
    """
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()
        # error
        # if not front_is_clear():
        #     turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
