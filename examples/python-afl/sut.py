import sys
import afl
import os

"""
https://github.com/jwilk/python-afl
https://barro.github.io/2018/01/taking-a-look-at-python-afl/
"""

def main(data):
    if len(data) == 50:
        if b'###' in data:
            if data.startswith(b"###"):
                if b"aaa" in data:
                    raise Exception("foo")

single = False

# Single execution
if single:
    afl.init()
    main(sys.stdin.buffer.read())
    os._exit(0) # makes things faster
else:
    # Multiple executions per process
    while afl.loop(10000):
        main(sys.stdin.buffer.read())
        sys.stdin.buffer.seek(0)