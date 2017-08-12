#!/usr/bin/python 2.7

import time
import webbrowser


def take_a_break(total_breaks):
    """Once run, makes the user take breaks depending on the input."""
    break_count = 0
    print "This program started on " + time.ctime()
    while break_count < total_breaks:
        time.sleep(10)  # 2 * 60 * 60 = 2 hours
        print "The time is now " + time.ctime()
        print "Get ready to dance...."
        time.sleep(3)
        webbrowser.open('https://youtu.be/xo1VInw-SKc', new=2)
        break_count += 1


take_a_break(3)
