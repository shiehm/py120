"""
Advanced challenge: 
Modify this class so that the __init__ method optionally lets you specify a 
fixed banner width when the Banner object is created. The message in the banner 
should be centered within the banner of that width. Decide for yourself how you 
want to handle widths that are either too narrow or too wide.

So there are a couple of options:
1. Wrap the text onto the next line, this will be harder
2. Cut the text, just don't show anything that doesn't fit

I'll do #2 first. 
There was a tricky part, where I had to do the alterations to the message in the 
property setter, not the initializer. 

For #1, I believe adding newlines would solve it. This can be a helper function 
Simple Algorithm:
1. Split the words into a list using split 
2. Starting with one line at a time, add the next word from the split list if 
   the line will remain less than the max
3. If it'll exceed the max, then append the line to result (if there is one) 
4. Do this until all words have been added

Notes:
- Remember that message contains '| ' in the beginning and ' |' at the end 
- Issue I fixed with join, when I joined ['word', ''] using ' '.join it created
  an extra space that was messing up the remaining_space
"""

def wrap_text(message: str, max_width: int):
    if not message:
        return '| ' + ' ' * max_width + ' |'
    
    def create_line(current_line: list[str], current_line_length: int):
        # len(current_line) - 1 accounts for the space in btwn words, less 1 at end
        # This function will only be called if current_line is not empty
        remaining_space = max_width - current_line_length - (len(current_line) - 1)
        complete_line = ' '.join(current_line) + f'{" " * remaining_space}'
        return '| ' + complete_line.center(max_width) + ' |'
    
    result = []
    current_line = []
    current_line_length = 0
    words = message.split()
    
    for word in words:
        # len(current_line) gives the correct number of spaces between existing + new
        # Until the last word, which doesn't need a space after it
        new_line_length = current_line_length + len(current_line) + len(word)
        
        if new_line_length <= max_width:
            current_line.append(word)
            current_line_length += len(word)
        else:
            if current_line:
                result.append(create_line(current_line, current_line_length))
            current_line = [word]
            current_line_length = len(word)
            
    # Add the last line if it exists
    if current_line:
        result.append(create_line(current_line, current_line_length))
        
    return '\n'.join(result)


class Banner:
    def __init__(self, message, width=20):
        # Validating here b/c self.min_width relies on message 
        # Need to set min_width here to avoid circulat dependency 
        if not isinstance(message, str):
            raise TypeError('message must be str')
        
        self.min_width = max([len(word) for word in message.split()] + [1])
        self.width = width
        self.message = message

    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be int')

        self._width = max(width, self.min_width)
    
    @property
    def message(self):
        return self._message
        
    @message.setter
    def message(self, message):
        # # Solution for cutting the text
        # main_message = message[:self.width] if len(message) >= self.width else message 
        # end_spaces = f"{' ' * (self.width - len(message))}"
        # self._message = f"| {main_message + end_spaces} |"
        
        # Solution for wrapping the text
        self._message = wrap_text(message, self.width)
        
    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {' ' * self.width} |"

    def _horizontal_rule(self):
        return f"+-{'-' * self.width}-+"

    def _message_line(self):
        return self.message


# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

banner.message = "Hello my name is Melvin"
print(banner)

banner = Banner('123 this is 123 this is 123')
print(banner)

banner = Banner('123 this is 123 this is 123', 36)
print(banner)

banner = Banner('123 this is 123 this is 123', 15)
print(banner)

banner = Banner('123 this is 123 this is 123', 1)
print(banner)

banner = Banner('123 this is 123 this is 123', 70)
print(banner)