class Transform(str):
    def __new__(cls, content):
        return super().__new__(cls, content)
    
    def uppercase(self):
        return self.upper()
    
    def lowercase(self):
        return self.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz

# Launch School Solution:

class Transform:
    def __init__(self, data):
        self.data = data

    def uppercase(self):
        return self.data.upper()

    @classmethod
    def lowercase(cls, text):
        return text.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz