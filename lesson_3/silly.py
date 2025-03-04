# If both x and y can be expressed as integers, compute the sum of the integer values of x and y.
# Otherwise, concatenate the string values of x and y.

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    @staticmethod
    def is_digit_or_int(num):
        int_validator = isinstance(num, int)
        str_validator = (isinstance(num, str) and num.isdigit())
        return int_validator or str_validator
    
    def __add__(self, other):
        if self.is_digit_or_int(self.value) and self.is_digit_or_int(other):
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)