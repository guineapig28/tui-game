#!/usr/bin/env python3
import curses
import curses.ascii
 
def mainloop(scr):
    y = 2
    x = 2
    curses.curs_set(0)
    scr.keypad(True)

    scr.addstr(y,x, "o")
    while True:
        curses.halfdelay(10)
        ch = scr.getch()
        if ch == -1:
            x += 1
        elif ch == 113:     # q=quit
            break
        else:
            y += 1

        scr.erase()
        scr.addstr(y,x, "o")
        scr.refresh()
     
curses.wrapper(mainloop)
