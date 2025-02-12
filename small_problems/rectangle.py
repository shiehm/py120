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


rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True