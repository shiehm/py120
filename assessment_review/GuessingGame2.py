import random
import math

class GuessingGame:
    def __init__(self):
        self.low = None
        self.high = None
        self.guesses = None
        self.reset()
        
    def reset(self):
        low = input('Input the low end of the range: ')
        while not (low.isdigit() and int(low) >= 0):
            low = input('Input a valid positive number: ')
        self.low = int(low)
        
        high = input('Input the high end of the range: ')
        while not(high.isdigit() and int(high) >= self.low):
            high = input(f'Input a valid number greater than {self.low}')
        self.high = int(high)
        
        self.answer = random.randint(self.low, self.high)
        self.guesses = int(math.log2(self.high - self.low + 1)) + 1
    
    
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
                        print(f'The answer was {self.answer}')
            
            play_again = input('Play again? Y/N: ')
            while play_again.casefold()[0] not in ['y', 'n']:
                play_again = input('Play again? Y/N: ')
            if play_again.casefold()[0] == 'n':
                break
            self.reset()

game = GuessingGame()
game.play()