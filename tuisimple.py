#!/usr/bin/env python3

# pylint: disable=invalid-name
# pylint: disable=line-too-long

""" Terminal Game """

import curses
import random

def mainloop(scr):
    """ main event loop """
    xvel = 1
    yvel = 0
    y = 10
    x = 5
    xtarget = random.randint(1, 79)
    ytarget = random.randint(2, 24)
    brake = 2
    score = 0
    snake = [ [1, 10], [2, 10], [3, 10], [4, 10], [5, 10] ]

    # Hide the cursor
    curses.curs_set(0)

    scr.addstr(y, x, "Z")
    while True:

        # Wait one second for user input
        # If no key pressed, continue anyway (after one second)
        curses.halfdelay(brake)

        # ch gets value of pressed key
        ch = scr.getch()

        if ch == 113:       # q=quit
            break
        elif ch == 258:
            yvel = 1
            xvel = 0
        elif ch == 261:
            xvel = 1
            yvel = 0
        elif ch == 259:
            yvel = -1
            xvel = 0
        elif ch == 260:
            xvel = -1
            yvel = 0
        elif ch == 32:
            xvel = 0
            yvel = 0
        elif ch == 49:
            brake = 1
        elif ch == 50:
            brake = 2
        elif ch == 51:
            brake = 3
        elif ch == 52:
            brake = 4
        elif ch == 53:
            brake = 5
        elif ch == 54:
            brake = 6
        elif ch == 55:
            brake = 7
        elif ch == 56:
            brake = 8
        elif ch == 57:
            brake =9
#       elif ch == 27:
#           score = score + 1749
        # Advance
        x = x + xvel
        y = y + yvel

        # Check if we're at the target
        if x == xtarget and y == ytarget:
            xtarget = random.randint(0,50)
            ytarget = random.randint(0,25)
            score = score + 1
        scr.erase()

        # print something at position x, y
        scr.addstr(y, x, "Z")
        scr.addstr(ytarget, xtarget, "T")

        # draw snake
        snake.pop(0)
        snake.append([x,y])
        for sx, sy in snake:
            scr.addstr(sy, sx, "z")

        scr.addstr(0, 0, "ch={} x={} y={} xvel={} yvel={} brake={} score={}".format(ch, x, y, xvel, yvel, brake, score))
        scr.refresh()

curses.wrapper(mainloop)
