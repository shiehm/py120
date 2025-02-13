"""
Your task is to write a CircularBuffer class in Python that implements a 
circular buffer for arbitrary objects. The class should be initialized with 
the buffer size and provide the following methods:

put: Add an object to the buffer
get: Remove (and return) the oldest object in the buffer. 
Return None if the buffer is empty.

You may assume that none of the values stored in the buffer are None 
(however, None may be used to designate empty spots in the buffer).

Data Structure:
- We can create a list, since lists are ordered and sequential 
    - [X, X, X, X, X]
    - We can have a counter that resets to 0 after the maximum 
    - Will need an instance variable that tracks the current place 

Notes:
- For the initialization, we need the number of spots
- We can initialize the list with None
- What we need is a way to:
    - Go up in count as we `put` objects into the buffer
    - Reset the index to 0 when we reach the max 
    - Replace objects that we `get` with None
    - Track the oldest place in a stand alone method 
"""

class CircularBuffer:
    
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = [None for i in range(buffer_size)]
        self.current_place = 0
        self.total_count = 0
        self.oldest_place = 0
    
    def put(self, put_object):
        """
        We need to:
        1. Replace the current_place index with the put_object
        2. Change the oldest_place to the index right after the current_place
        3. Increment current_place by 1 (accounting for circular at last index)
        - If the buffer is already filled, the oldest_place == current_place 
        - If the buffer is not yet filled, the oldest_place == 0 
        - Actually no, because if get is used, then current place can mis-align,
          it needs to be counted separately
        """
        # This needs to come first to see if anything was over-written
        # If it was, that means the oldest is the one following 
        # If not, oldest_place will remain what is was
        if self.buffer[self.current_place]:
            self.oldest_place = (self.current_place + 1) % self.buffer_size
        
        self.buffer[self.current_place] = put_object
        self.current_place = (self.current_place + 1) % self.buffer_size
        self.total_count += 1
        
    def get(self):
        """
        Functionality:
        - Return the oldest_place 
        - If get returns None, do not change the index (or rather, can only)
          use get if there is a valid non-null object to be gotten
        - It should only be None if the buffer has not yet been filled 
        """
        popped_object = self.buffer[self.oldest_place]
        self.buffer[self.oldest_place] = None
        
        if popped_object != None:
            self.oldest_place = (self.oldest_place + 1) % self.buffer_size
            return popped_object
        
        return None
        
        # self.total_actions += 1
        # print(f"Oldest index: {oldest_index}")
        # print(f"Current buffer: {self.buffer}")
        # print(f"Popped object: {popped_object}")

"""
True or False below
"""

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
print()

"""
Showing the output below
"""

buffer = CircularBuffer(3)
print(buffer.get())             # None

buffer.put(1)
buffer.put(2)
print(buffer.get())             # 1

buffer.put(3)
buffer.put(4)
print(buffer.get())             # 2

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get())             # 5
print(buffer.get())             # 6
print(buffer.get())             # 7
print(buffer.get())             # None


buffer2 = CircularBuffer(4)
print(buffer2.get())            # None

buffer2.put(1)
buffer2.put(2)
print(buffer2.get())            # 1

buffer2.put(3)
buffer2.put(4)
print(buffer2.get())            # 2

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get())          # 4
print(buffer2.get())          # 5
print(buffer2.get())          # 6
print(buffer2.get())          # 7
print(buffer2.get())          # None


"""
This is a really ingenious solution, in that it doesn't care about the exact 
places but rather makes index 0 always the oldest, and always trims the size 
of the list to match buffer size.

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = []

    def put(self, object):
        if len(self.buffer) == self.size:
            self.buffer.pop(0)                       

        self.buffer.append(object)

    def get(self):
        return self.buffer.pop(0) if self.buffer else None
"""