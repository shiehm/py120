# PEDAC
# calculate which index is currently "selected"
# Have a mechanism for moving the selected by 1 when something is added
# calculate which index is the oldest 
# move the oldest if it gets overridden or removed 

class CircularBuffer:
    def __init__(self, length):
        self.length = length
        self.buffer = [None] * length
        self.oldest = 0
        self.current = 0

    def put(self, num):    
        self.buffer[self.current] = num
        self.current += 1
        self.current %= self.length
        if self.buffer[self.current] != None:
            self.oldest = self.current

    def get(self):
        if self.buffer[self.oldest] is None:
            return None
        item = self.buffer.pop(self.oldest)
        self.buffer.insert(self.oldest, None)
        self.oldest += 1
        self.oldest %= self.length
        return item

    def __str__(self):
        return f'{self.buffer}'
    
buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True