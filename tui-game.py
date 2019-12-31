#!/usr/bin/env python3

import curses
 
def mainloop(scr):
    xvel = 0
    yvel = 0
    y = 10
    x = 10

    # Hide the cursor
    curses.curs_set(0)

    scr.addstr(y,x, "Z")
    while True:

        # Wait one second for user input
        # If no key pressed, continue anyway (after one second)
        curses.halfdelay(10)

        # ch gets value of pressed key
        ch = scr.getch()

#        if ch == -1:        # no key was pressed
#            x = x + 1
        if ch == 113:       # q=quit
            break
        elif ch == 258:
            yvel = 1
        elif ch == 261:
            xvel = 1
            yvel = 0
        elif ch == 32:
            xvel = 0
            yvel = 0

        x = x + xvel
        y = y + yvel

        scr.erase()

        # print something at position x, y
        scr.addstr(y,x, "Z")

        scr.addstr(0,0,"ch={} x={} y={} xvel={} yvel={}".format(ch, x, y, xvel, yvel))
        scr.refresh()
     
curses.wrapper(mainloop)

