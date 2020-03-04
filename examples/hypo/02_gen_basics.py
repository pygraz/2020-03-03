import pytest
import string

from hypothesis.strategies import (
    binary, booleans, characters, complex_numbers,
    dates, datetimes, decimals, dictionaries, emails, floats,
    integers, just, lists, none, one_of, permutations, sampled_from,
    slices, text, uuids, times, tuples, fixed_dictionaries, from_regex,
    from_type, register_type_strategy, composite, sets)
from hypothesis import given, infer

# Example on how to use a strategy
@given(binary())
def my_test(value):
    pass

# Basic types
for i in range(10):
    pass
    #print(binary().example())
    #print(booleans().example())
    #print(characters().example())
    #print(complex_numbers().example())
    #print(floats().example())
    #print(integers().example())
    #print(repr(text().example()))
    #print(repr(text(string.printable).example()))
    #print(none().example())
    #print(decimals().example())
    #print(slices(42).example())

# Other types
for i in range(10):
    pass
    #print(datetimes().example())
    #print(emails().example())
    #print(dates().example())
    #print(uuids().example())
    #print(times().example())

# Meta
for i in range(10):
    pass
    #print(just(value=42).example())
    #print(lists(integers()).example())
    #print(one_of(integers(), none()).example())
    #print(permutations([1, 2, 3]).example())
    #print(sampled_from([1, 2, 3, 4]).example())
    #print(dictionaries(keys=integers(), values=dates()).example())
    #print(tuples(integers(), uuids(), times()).example())
    #print(sets(integers()).example())
    #print(fixed_dictionaries({"foo": integers(), "bar": dates()}).example())

# Other fancy things:
class MyType():
    pass

register_type_strategy(MyType, lambda t: just(value=t()))

for i in range(10):
    pass
    #print(from_regex(r"->a+", True).example())
    #print(from_type(MyType).example())