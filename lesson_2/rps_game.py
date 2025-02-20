import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')
    
    def __init__(self):
        self.move = None

class Human(Player):
    def __init__(self):
        super().__init__()
    
    def choose(self):
        # Public method b/c RPSGame calls it
        # This method is how the player chooses rock, paper or scissors
        print(f'Choose a move in {Player.CHOICES}')
        choice = input().lower()
        while choice not in Player.CHOICES:
            print(f'Choose a move in {Player.CHOICES}')
            choice = input().lower()
        self.move = Move(choice)

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = random.choice(Player.CHOICES)
        self.move = Move(choice)

class Move:
    def __init__(self, choice):
        self._choice = choice
    
    def __str__(self):
        return str(self._choice)
    
    # Only needs this one class because this is the only one used >
    def __gt__(self, other):
        if not isinstance(other, Move):
            raise TypeError('Can only compare 2 Move class objects.')
        
        return (
            (self._choice == 'rock' and other._choice == 'scissors') or
            (self._choice == 'paper' and other._choice == 'rock') or
            (self._choice == 'scissors' and other._choice == 'paper')
            )

# Start here, this is the proceedure of the game
class RPSGame:
    def __init__(self):
        # The Player objects are collaborators of RPSGame
        self._human = Human()
        self._computer = Computer()
        
    def display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')
    
    def display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')
    
    def _human_wins(self):
        return self._human.move > self._computer.move

    def _computer_wins(self):
        return self._computer.move > self._human.move

    def display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')
        
        if self._human_wins():
            print('Player Wins!')
        elif self._computer_wins():
            print('Computer Wins!')
        else:
            print('Tie!')

    def _play_again(self):
        print('Play again? Y/N')
        choice = input()[0].upper()
        return choice == 'Y'
    
    def play(self):
        self.display_welcome_message()
        
        while True:
            self._human.choose()
            self._computer.choose()
            self.display_winner()
            if not self._play_again():
                break
        
        self.display_goodbye_message()
        
game = RPSGame()
game.play()
