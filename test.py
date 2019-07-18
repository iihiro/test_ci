#!/bin/env python
## -*- coding: utf-8 -*-

from a import A
import pytest

@pytest.fixture(scope = "module")
def calc():
    c = A()
    print("create A")
    return c

def test_add(calc):
    assert calc.add(2, 1) == 3
    
#def test_div(calc):
#    assert calc.div(2, 1) == 2
#
#def test_square(calc):
#    assert calc.square(2) == 4
#    
#def test_cube(calc):
#    assert calc.cube(2) == 8
