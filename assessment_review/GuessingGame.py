"""
Problem:
- Create a guessing game where the player has X guesses to guess a number between a low and high point.
- Game will tell you if you are too low or too high before the next guess

Algorithm:
- Input a guess
- Validate the guess: is it a number, is it within the range?
- Assess whether the guess is too high, too low, or right
- If not right, decrement the guess count
- If guess count reaches 0 it's game over
"""

import random

class GuessingGame:
    def __init__(self, low=0, high=100, guesses=7):
        self.low = low
        self.high = high
        self.initial_guesses = guesses
        self.guesses = guesses
        self.reset()
        
    def reset(self):
        self.answer = random.randint(self.low, self.high)
        self.guesses = self.initial_guesses

    def valid(self, num):
        if num.isdigit() and (self.low <= int(num) <= self.high):
            return True
        return False

    def win(self, num):
        if num == self.answer:
            return True
        return False

    def feedback(self, num):
        if num < self.answer:
            return 'Your guess is too low'
        else:
            return 'Your guess is too high'
    
    def play(self):   
        while True:
            while self.guesses > 0:
                
                print(f'You have {self.guesses} guesses left.')
                guess = None
                while not guess:
                    response = input(f'Enter a number between {self.low} and {self.high}: ')
                    if self.valid(response):
                        guess = int(response)
                
                if self.win(guess):
                    print('You won!')
                    break
                else:
                    print(self.feedback(guess))
                    self.guesses -= 1
                    if self.guesses == 0:
                        print('You have no more guesses. You lost!')
            
            play_again = input('Play again? Y/N: ')
            while play_again.casefold()[0] not in ['y', 'n']:
                play_again = input('Play again? Y/N: ')
            if play_again.casefold()[0] == 'n':
                break
            self.reset()

game = GuessingGame()
game.play()