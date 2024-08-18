# import pytest
# from source.shapes import Square

"""
Class-based approach using, well, classes
"""
### uncomment lines 1 and 2 to use the class-based test

# class TestSquare:
#     def setup_method(self):
#         self.square = Square('Test Square', 5)
#         print (f"setting up {self.square.name}...")
    
#     def teardown_method(self):
#         print (f"tearing down {self.square.name}...")
#         del self.square
#         print("done!")
    
#     def test_area(self):
#         assert self.square.area() == 25
    
#     def test_perimeter(self):
#         assert self.square.perimeter() == 20

"""
Functional-based approach using fixtures
"""
def test_perimeter(square):
    assert square.perimeter() == 20

def test_area(square):
    assert square.area() == 25

def test_equality(square):
    assert square == Square('Test Square', 5)

def test_inequality(square):
    assert square != Square('Test Square', 4)

def test_str(square):
    assert str(square) == 'Test Square square with side length 5'

def test_equality_with_negative_side(square_with_negative_side):
    with pytest.raises(ValueError):
        square_with_negative_side == Square('Test Negative Square', -5)

@pytest.mark.parametrize("length, expected_area", [(5, 25), (3, 9), (1.3, 1.69), (1, 1), (26, 676), (4.8, 23.04)])
def test_multiple_square_areas(blank_square, length, expected_area):
    assert blank_square(length).area() == expected_area

