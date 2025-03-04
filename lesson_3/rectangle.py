class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

rectangle = Rectangle(3, 6)
print(rectangle.width)
print(rectangle.height)
rectangle.width = 8