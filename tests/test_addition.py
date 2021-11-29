import pytest
from Operation.addition import addition

def test_add_positive():
    assert addition(5,6) == 11

def test_add_negative():
    assert addition(-3,-2) == -5

def test_add_strings():
    with pytest.raises(TypeError):
        addition(5,"Invalid")