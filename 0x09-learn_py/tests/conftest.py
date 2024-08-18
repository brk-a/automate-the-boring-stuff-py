import pytest
from source.shapes import Square

@pytest.fixture
def square():
    return Square('Test Square', 5)

@pytest.fixture
def square_with_negative_side():
    return Square('Test Negative Square', -5)

@pytest.fixture
def blank_square(length):
    return Square('Test Square', length)