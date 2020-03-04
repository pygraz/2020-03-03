import pytest
from string import printable

from hypothesis.strategies import (
    binary, booleans, characters, complex_numbers,
    dates, datetimes, decimals, dictionaries, emails, floats,
    integers, just, lists, none, one_of, permutations, sampled_from,
    slices, text, uuids, times, recursive)
from hypothesis import given, assume, infer

# Map, Filter, Assume, Flatmap, Recursion

# filter()
@given(integers(min_value=0).filter(lambda i: i % 100 == 0))
def test_even(value):
    print(value)

# assume()
@given(integers(min_value=0))
def test_even2(value):
    assume(value % 2 == 0)
    print(value)

# map()
@given(integers(min_value=0).map(lambda i: i * 2))
def test_even3(value):
    print(value)

# flatmap()
@given(
    integers(min_value=2, max_value=3).flatmap(
        lambda n: lists(integers(min_value=0).filter(
            lambda i: i % n == 0))))
def test_all_mod_same(values):
    print(values)

# Recursion()
@given(
    recursive(none() | booleans() | floats() | text(printable),
        lambda children: lists(children, 1) | dictionaries(text(printable), children, min_size=1))
)
def test_recursive(x):
    print(x)

# Strategies inferred from annotations
@given(bla=infer, foo=infer)
def test_foo(bla: int, foo: str):
    print(bla, foo)