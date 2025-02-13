"""
We took a straightforward approach here and implemented a single class. 
Do you think it would be a good idea to have a Player class? What methods and 
data should be part of it? How many Player objects do you need? Should you use 
inheritance, a mix-in module, or a collaborative object?

"""

import random

class GuessingGame:
    def __init__(self, low=1, high=100, guesses=7):
        self.low = low
        self.high = high
        self.number = random.randint(low, high)
        self.guesses = guesses
    
    def validate(self, number):
        if not isinstance(number, int):
            raise TypeError('Input must be an integer')
        if number > self.high or number < self.low:
            raise ValueError(f'Invalid guess. Enter an integer between {self.low} and {self.high}')
        return number
    
    def play(self):
        while True:
            if self.guesses == 0:
                print('You have no more guesses. You lost!')
                break
            
            print(f'You have {self.guesses} guesses remaining')
            print(f'Enter a number between {self.low} and {self.high}: ')
            x = self.validate(int(input()))
            if x < self.number:
                print('Your guess is too low.')
                self.guesses -= 1
            elif x > self.number:
                print('Your guess is too high.')
                self.guesses -= 1
            else:
                print('That is the number! You Won!')
                break


game = GuessingGame()
game.play()