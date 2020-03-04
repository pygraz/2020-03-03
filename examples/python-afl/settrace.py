'''
https://docs.python.org/3/library/sys.html#sys.settrace
'''

import time
import sys

# TRACING

def gettracefunc(level=0):
    def wrap(frame, event, arg):
        print(level * 4 * " ", [event, frame, arg])
        if event == "call":
            return gettracefunc(level + 1)
        return gettracefunc(level)
    return wrap

tracefunc = gettracefunc()
current_frame = sys._getframe()

# Set the global trace function
sys.settrace(tracefunc)
# Also trace the current frame, as settrace only starts from calls
# current_frame.f_trace = tracefunc

# SYSTEM UNDER TEST

def error():
    raise Exception("oops")

def error2():
    time.sleep(99999)

def mytestfunction(value):
    if "###" in value:
        if "aaa" in value:
            error()
        if "bbb" in value:
            error2()

mytestfunction("###")