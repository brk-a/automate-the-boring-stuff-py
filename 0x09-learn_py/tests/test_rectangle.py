import pytest
from ssource.shapes import Rectangle

@pytest.fixture
def rectangle():
    return Rectangle('Test Rectangle', 5, 3)

@pytest.fixture
def rectangle_with_negative_dimensions():
    return Rectangle('Test Negative Rectangle', -5, 3)

def test_area(rectangle):
    assert rectangle.area() == 15

def test_perimeter(rectangle):
    assert rectangle.perimeter() == 16

def test_equality(rectangle):
    assert rectangle == Rectangle('Test Rectangle', 5, 3)

def test_inequality(rectangle):
    assert rectangle != Rectangle('Test Rectangle', 5, 4)

def test_str(rectangle):
    assert str(rectangle) == 'Test Rectangle rectangle with width 5 and length 3'

def test_equality_with_negative_dimensions(rectangle_with_negative_dimensions):
    with pytest.raises(ValueError):
        rectangle_with_negative_dimensions == Rectangle('Test Negative Rectangle', -5, 3)

