class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def _validate(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError('Inputs for width and height be numbers')
        return amount
    
    @property 
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        self._width = self._validate(width)
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = self._validate(height)
    
    @property
    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

square = Square(5)
print(square.area == 25)      # True