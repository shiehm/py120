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
        self.move = input().lower()

        while self.move not in Player.CHOICES:
            print(f'Choose a move in {Player.CHOICES}')
            self.move = input().lower()

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

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
        return (
            (self._human.move == 'rock' and self._computer.move == 'scissors') or
            (self._human.move == 'paper' and self._computer.move == 'rock') or
            (self._human.move == 'scissors' and self._computer.move == 'paper')
            )
    
    def _computer_wins(self):
        return (
            (self._human.move == 'rock' and self._computer.move == 'paper') or
            (self._human.move == 'paper' and self._computer.move == 'scissors') or
            (self._human.move == 'scissors' and self._computer.move == 'rock')
            )
    
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
