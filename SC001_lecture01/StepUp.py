"""
File: StepUp.py
Name: Jasper
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *
def turn_right():
    """
    定義右轉
    """
    turn_left()
    turn_left()
    turn_left()

def put_99beeper():
    """
    使用for迴圈放99個beeper
    """
    for i in range(99):
        put_beeper()

def main():
    pass
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    put_99beeper()
    move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
