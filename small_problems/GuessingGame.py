import random
import math

class GuessingGame:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.number = random.randint(low, high)
        self.guesses = int(math.log2(high - low + 1)) + 1
    
    def validate(self, number):
        if not number.isdigit():
            return False
        if self.low > int(number) or self.high < int(number):
            return False
        return True
    
    def play(self):
        while True:
            if self.guesses == 0:
                print('You have no more guesses. You lost!')
                print(f'The number was {self.number}')
                break
            
            print(f'You have {self.guesses} guesses remaining')
            print(f'Enter a number between {self.low} and {self.high}: ')
            
            x = input()
            while not self.validate(x):
                print(f'Invalid response. Please input an integer from {self.low} to {self.high}')
                x = input()
            x = int(x)
            
            if x < self.number:
                print('Your guess is too low.')
                self.guesses -= 1
            elif x > self.number:
                print('Your guess is too high.')
                self.guesses -= 1
            else:
                print('That is the number! You Won!')
                break


game = GuessingGame(1, 9999)
game.play()