import pytest

from hypothesis.strategies import (
    binary, booleans, characters, complex_numbers,
    dates, datetimes, decimals, dictionaries, emails, floats,
    integers, just, lists, none, one_of, permutations, sampled_from,
    slices, text, uuids, times, recursive, composite, data)
from hypothesis import given, assume


####################################################
# no composite

@given(integers(0, 255), integers(0, 255), integers(0, 255))
def test_with_color(a, b, c):
    color = "#%02X%02X%02X" % (a, b, c)
    print(color)


####################################################
# composite
@composite
def my_special_strategy(draw, short=False):
    if short:
        s = integers(0, 15)
        return "#%01X%01X%01X" % (draw(s), draw(s), draw(s))
    else:
        l = integers(0, 255)
        return "#%02X%02X%02X" % (draw(l), draw(l), draw(l))

@given(my_special_strategy(short=False))
def test_something(color):
    print(color)

####################################################
# composite: show shrinking

@composite
def my_special_strategy2(draw):  # draw() is like strategy().example()
    i = integers(0, 255)
    x = []
    for _ in range(draw(i)):
        x.append(draw(i))
    return x

#@given(lists(integers(0, 255), min_size=0, max_size=255)))
@given(my_special_strategy2())
def test_something2(numbers):
    print(numbers)
    if sum(numbers) > 100 and len(numbers) > 11:
        raise Exception()

# https://github.com/pygobject/pycairo/blob/master/tests/hypothesis_fspaths.py

####################################################
# using data()

@given(data())
def test_something3(data):
    i = integers(0, 255)

    numbers = []
    for x in range(data.draw(i, "list length")):
        numbers.append(data.draw(i, "list item #%d" % x))

    if sum(numbers) > 100 and len(numbers) > 11:
        raise Exception()
