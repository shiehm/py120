import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    
    def __init__(self):
        self.move = None
        self.score = 0
        self._history = []
        
    @property
    def history(self):
        return self._history[::-1]

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
        self.move = Move.create_move(choice)
        self._history.append(choice)

class Computer(Player):
    PERSONALITIES = ('normal', 'r2d2', 'hal', 'daneel')
    
    def __init__(self):
        super().__init__()
        self._human = None
    
    def set_human(self, human):
        self._human = human
    
    @classmethod
    def create_computer(cls, choice):
        personalities = {
            'normal': Normal(),
            'r2d2': R2d2(), 
            'hal': Hal(),
            'daneel': Daneel()
        }
        return personalities[choice]

class Normal(Computer):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = random.choice(Player.CHOICES)
        self.move = Move.create_move(choice)
        self._history.append(choice)

class R2d2(Computer):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = 'rock'
        self.move = Move.create_move(choice)
        self._history.append(choice)

class Hal(Computer):
    def __init__(self):
        super().__init__()

    def choose(self):
        hal_choices = ('rock', 'paper', 'scissors', 'scissors', 'scissors', 'scissors', 'lizard', 'spock')
        choice = random.choice(hal_choices)
        self.move = Move.create_move(choice)
        self._history.append(choice)

class Daneel(Computer):
    def __init__(self):
        super().__init__()
    
    def choose(self):
        choice = self._human.history[0]
        self.move = Move.create_move(choice)
        self._history.append(choice)

class Move:
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__
    
    def move_validator(self, other):
        if not isinstance(other, Move):
            raise TypeError('Can only compare 2 Move sub-class objects.')
    
    @classmethod
    def create_move(cls, choice):
        possible_moves = {
            'rock': Rock(), 
            'paper': Paper(), 
            'scissors': Scissors(), 
            'lizard': Lizard(), 
            'spock': Spock()
        }
        return possible_moves[choice]
    
class Rock(Move):
    def __gt__(self, other):
        self.move_validator(other)
        return isinstance(other, (Scissors, Lizard))

class Paper(Move):
    def __gt__(self, other):
        self.move_validator(other)
        return isinstance(other, (Rock, Spock))

class Scissors(Move):
    def __gt__(self, other):
        self.move_validator(other)
        return isinstance(other, (Paper, Lizard))

class Lizard(Move):
    def __gt__(self, other):
        self.move_validator(other)
        return isinstance(other, (Paper, Spock))

class Spock(Move):
    def __gt__(self, other):
        self.move_validator(other)
        return isinstance(other, (Scissors, Rock))

# Start here, this is the proceedure of the game
class RPSGame:
    def __init__(self):
        # The Player objects are collaborators of RPSGame
        self.new_game()
    
    @property
    def human(self):
        return self._human
    
    def create_computer(self):
        personality = random.choice(Computer.PERSONALITIES)
        computer = Computer.create_computer(personality)
        computer.set_human(self._human)
        return computer
        
    def get_games(self):
        while True:
            games = input('How many games do you want to play? ')
            if games.isdigit():
                self._total_games = int(games)
                break
            print('Invalid response, please enter a digit')
        
    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')
    
    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')
    
    def _human_wins(self):
        return self._human.move > self._computer.move

    def _computer_wins(self):
        return self._computer.move > self._human.move
        
    def _display_score(self):
        print(f'Human Score: {self._human.score}')
        print(f'Computer Score: {self._computer.score}')

    def _display_round_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')
        
        if self._human_wins():
            self._human.score += 1
            print('Player Wins!')
        elif self._computer_wins():
            self._computer.score += 1
            print('Computer Wins!')
        else:
            print('Tie!')
    
    def _continue_playing(self):
        return max(self._human.score, self._computer.score) < (self._total_games / 2)
    
    def _display_winner(self):
        if self._human.score > self._computer.score:
            print(f'Player Wins {self._human.score} out of {self._total_games} games!')
        else:
            print(f'Computer Wins {self._computer.score} out of {self._total_games} games!')
    
    def _display_history(self):
        print('Display history of moves? (Y/N)')
        choice = input()
        if choice.lower().startswith('y'):
            print('Most recent moves shown first: ')
            print(f'Previous Player Moves: {self._human.history}')
            print(f'Previous Computer Moves: {self._computer.history}')
    
    def _play_again(self):
        print('Play again? Y/N')
        choice = input()[0].upper()
        return choice == 'Y'
    
    
    # NEED TO FIX BELOW BUT RIGHT IDEA:
    def new_game(self):
        self._human = Human()
        self._computer = self.create_computer()
        self._human.score = 0
        self._computer.score = 0
        self._total_games = 0

    def play(self):
        self._display_welcome_message()
        while True:
            self.get_games()
            while self._continue_playing():
                if self._human.history:
                    self._display_history()
                self._human.choose()
                self._computer.choose()
                self._display_round_winner()
                self._display_score()
            self._display_winner()
            if not self._play_again():
                break
            self.new_game()
        self._display_goodbye_message()
        
game = RPSGame()
game.play()
