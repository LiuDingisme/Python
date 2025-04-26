"""
File: PotholeFilling.py
Name: Jasper
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def go_in():
    """
    pre-condition:karel的初始位置在洞口上方面東邊
    post-condition:karel在洞裡且面向北方
    """
    move()
    turn_right()
    move()
    turn_left()
    turn_left()

def go_out():
    """
    pre-condition:karel在洞裡面向北方
    post-condition:karel的結束位置在洞口上方面東邊
    """
    move()
    turn_right()
    move()

def main():
    """
    進入洞裡並放入99beeper
    """
    pass
    for i in range(3):
        go_in()
        put_99beeper()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
