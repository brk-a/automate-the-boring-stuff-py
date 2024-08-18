import math
import pytest
from shapes import Circle


class TestCircle:
    def setup_method(self):
        self.circle = Circle('Test Circle', 5)
        print (f"setting up {self.circle.name}...")
    
    def teardown_method(self):
        print (f"tearing down {self.circle.name}...")
        del self.circle
        print("done!")
    
    def test_area(self):
        assert self.circle.area() == pytest.approx(78.53981633974483)
        assert self.circle.area() == math.pi * (self.circle.radius ** 2)
    
    def test_perimeter(self):
        assert self.circle.perimeter() == pytest.approx(31.41592653589793)
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
    
    def test_equality(self, square):
        assert self.circle == Circle('Test Circle', 5)
        assert self.circle.__eq__(square)
