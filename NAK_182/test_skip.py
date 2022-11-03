import sys
import math_func
import pytest

@pytest.mark.skip(reason="just wanna skip it")
def test_add():
    assert math_func.add(4,3) == 7
    assert math_func.add(6) == 10

@pytest.mark.skipif(sys.version_info > (3,10), reason="requires python 3.x")
def test_product():
    assert math_func.product(6,5) == 30
    assert math_func.product(2) == 4

@pytest.mark.xfail
def test_greater_equal():
   num = 100
   assert num >= 100



