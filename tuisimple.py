#!/usr/bin/env python3

# pylint: disable=invalid-name
# pylint: disable=line-too-long

""" Terminal Game """

import curses
import random

def mainloop(scr):
    """ main envent loop """
    xvel = 0
    yvel = 0
    y = 10
    x = 10
    xtarget = random.randint(0,50)
    ytarget = random.randint(0,25)
    brake = 2

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
        elif ch == 119:
            brake = brake + 1
        elif ch == 115:
            brake = brake - 1
        x = x + xvel
        y = y + yvel

        # Check if we're at the target
        if x == xtarget and y == ytarget:
            xtarget = random.randint(0,50)
            ytarget = random.randint(0,25)

        scr.erase()

        # print something at position x, y
        scr.addstr(y, x, "Z")
        scr.addstr(ytarget, xtarget, "T")

        scr.addstr(0, 0, "ch={} x={} y={} xvel={} yvel={} brake={}".format(ch, x, y, xvel, yvel, brake))
        scr.refresh()

curses.wrapper(mainloop)
