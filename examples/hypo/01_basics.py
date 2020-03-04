def startswith_bug(text, part):
    if len(text) > 10:
        raise Exception("oops")
    return text[:len(part)] == part

#####################################

def startswith(text, part):
    return text[:len(part)] == part

#startswith = startswith_bug

#####################################

""" import unittest

class Test(unittest.TestCase):

    def test_startswith(self):
        self.assertTrue(startswith("foobar123456", "foo"))
        self.assertTrue(startswith("foobar", ""))
        self.assertFalse(startswith("foobar", "bar"))

if __name__ == '__main__':
    unittest.main() """

#####################################

""" def test_startswith():
    assert not startswith("foobar123456", "foo")
    assert startswith("foobar", "")
    assert not startswith("foobar", "bar") """

#####################################

""" import pytest

@pytest.mark.parametrize("input, expected", [
    (("foobar123456", "foo"), True),
    (("foobar", ""), True),
    (("foobar", "bar"), False),
])
def test_startswith(input, expected):
    assert startswith(*input) == expected
  """
#####################################


""" import pytest

@pytest.mark.parametrize("text", ["foobar123456", "bla", "quux"])
@pytest.mark.parametrize("part", ["foo", "bar", "", "nope", "x"])
def test_startswith(text, part):
    result = startswith(text, part)
    assert isinstance(result, bool)
    assert result in [True, False]
"""

#######################################

""" from hypothesis import given
from hypothesis.strategies import text

@given(text(), text())
def test_startswith(text, part):
    print([text, part])
    result = startswith(text, part)
 """
###################

""" import pytest
from hypothesis import given, example
from hypothesis.strategies import text

def test_startswith_static():
    assert startswith("000000000000", "")

#@example("000000000000", "")
@given(text(), text())
def test_startswith(text, part):
    try:
        result = startswith(text, part)
    except Exception:
        print(["FAIL", text, part])
        raise
    else:
        print(["OK  ", text, part])
 """

import pytest
from hypothesis import given, example
from hypothesis.strategies import text

@given(text(), text())
def test_startswith(a, b):
    text = a + b
    assert startswith(text, a)


###################

import pytest
import sqlite3
from hypothesis import given
from hypothesis.strategies import text

@pytest.fixture(scope="module")
def my_fancy_database():
    con = sqlite3.connect(":memory:")
    try:
        yield con
    finally:
        con.close()

@given(foo=text())
def test_fixture(my_fancy_database, foo):
    print(my_fancy_database, foo)