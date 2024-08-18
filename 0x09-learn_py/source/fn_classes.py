class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    @property
    def add(self):
        return self.num1 + self.num2
    
    @add.setter
    def add(self, value):
        self.num1 = value
    
    @add.deleter
    def add(self):
        del self.num1
        del self.num2

    def __str__(self):
        return f'Add object with num1: {self.num1} and num2: {self.num2}'
    
    def __add__(self, other):
        if isinstance(other, Add):
            return Add(self.num1 + other.num1, self.num2 + other.num2)
        else:
            raise TypeError('Unsupported operand type(s) for +: "Add" and "{type(other).__name__}"')