import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from type_test import add


def test_add():
    assert add(5, 10) == 15
    assert add("hello", " world") == "hello world"
    assert add(3.5, 2.5) == 6.0
    assert (
        add("cat", 1) == "TypeError: unsupported operand type(s) for +: 'str' and 'int'"
    )
