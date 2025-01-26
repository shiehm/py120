class Banner:
    def __init__(self, message, width=20):
        self.message = message
        self.width = width - 2
    
    @property
    def message(self):
        return self._message
        
    @message.setter
    def message(self, message):
        
        self._message = message
    
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
        return f"| {self.message} |"



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