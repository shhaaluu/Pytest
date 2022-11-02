import math_func
import pytest


@pytest.mark.number
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(3) == 5
    assert math_func.add(15) == 17

@pytest.mark.number
def test_product():
    assert math_func.product(3,3) == 9
    assert math_func.product(5) == 10
    assert math_func.product(3) == 7

@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello',' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result

@pytest.mark.string
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str

