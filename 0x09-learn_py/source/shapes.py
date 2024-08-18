class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise NotImplementedError('Subclasses must implement this method')
    
    def perimeter(self):
        raise NotImplementedError('Subclasses must implement this method')
    
    def __str__(self):
        return f'{self.name} shape'
    
    def __eq__(self, other):
        return isinstance(other, Shape) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f'{self.name} circle with radius {self.radius}'
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, Circle) and self.radius == other.radius
    

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__(name)
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return 4 * self.side_length
    
    def __str__(self):
        return f'{self.name} square with side length {self.side_length}'
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, Square) and self.side_length == other.side_length
    

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def __str__(self):
        return f'{self.name} rectangle with width {self.width} and length {self.length}'
    
    def __eq__(self, other):
        return super().__eq__(other) and isinstance(other, Rectangle) and self.width == other.width and self.length == other.length