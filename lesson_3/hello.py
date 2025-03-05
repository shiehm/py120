class Greeting:
    def greet(self, message):
        print(message)
    
    # @classmethod
    # def greet(cls, message):
    #     print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')
    
    @classmethod
    def hi(cls):
        Greeting().greet('hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')
        
Hello.hi()

"""
The problem now is that you can have a class method and an instance method with 
the same name in a class. However, if you try to use an instance of the class to 
call the instance method, Python will call the class method instead.

"""

hello = Hello()
hello.hi()