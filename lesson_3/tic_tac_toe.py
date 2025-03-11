"""
The OOO approach:
1. Write a textual description of the problem or exercise.
2. Extract the significant nouns and verbs from the description.
3. Organize and associate the verbs with the nouns.

Tic Tac Toe has 2 players making choices sequentially on a 9 square game board. 
The goal is to mark 3 squares in a row whether it is vertical, horizontal, or 
diagonal. One player is X and the other is O. Each turn, a player makes 1 choice 
leaving their marker on the board. After each move, the game will assess whether 
any player has marked 3 squares in a row. 
- 2 Players
- 3x3 Board
- Markers are X and O
- 1 choice is made each turn 
- Turns happen sequentially
- Win condition is 3 in a row, any way

Nouns:
- Game
- Game Board
    - Square
    - Row
- Players 
    - Player 1 and 2 or
    - Human and Computer
- Markers
    - X
    - O

Verb:
- Play 
- Choose (Player Behavior) 
- Assess winner 

Mapping:
- Players
    - Play
    - Choose
- Game
    - Assess Winner
"""

import random
import os

class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1,10)}
    
    def display(self):
        line = '---+---+---'
        print()
        print(f' {self.squares[1]} | {self.squares[2]} | {self.squares[3]} ')
        print(line)
        print(f' {self.squares[4]} | {self.squares[5]} | {self.squares[6]} ')
        print(line)
        print(f' {self.squares[7]} | {self.squares[8]} | {self.squares[9]} ')
    
    def mark_square(self, key, marker):
        self.squares[key].marker = marker
    
    def empty_squares(self):
        return [key for key, value in self.squares.items() if value.marker == Square.INITIAL_MARKER]
    
    def is_full(self):
        if not self.empty_squares():
            return True
        return False
    
class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"
    
    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker
    
    def __str__(self):
        return self.marker
    
    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker

class Player:
    def __init__(self, marker):
        self.marker = marker
    
    @property
    def marker(self):
        return self._marker
    
    @marker.setter
    def marker(self, marker):
        self._marker = marker

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

# Orchestration Engine: a class that controls the flow of the app / part of the app
class TTTGame:
    WINNING_COMBOS = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 5, 9),
            (3, 5, 7),
            (1, 4, 7),
            (2, 5, 9),
            (3, 6, 9)
            )
    
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.winner = None

    def play(self):
        self.display_welcome_message()
        
        while True:
            self.board.display()
            
            self.human_move()
            if self.is_game_over():
                break
            
            self.computer_move()
            if self.is_game_over():
                break
            
        self.board.display()
        self.display_results()
        self.display_goodbye_message()
    
    def display_results(self):
        if self.winner:
            print(f'The winner is {self.winner}!')
        else:
            print('It is a Tie!')
    
    def display_welcome_message(self):
        print('~Welcome~ to tic-tac-toe')
    
    def display_goodbye_message(self):
        print('~Thanks~ for playing tic-tac-toe!')
    
    def winning_rows(self, player, row):
        board_squares = self.board.squares
        markers = [board_squares[key].marker for key in row]
        return markers.count(player.marker)
    
    def three_in_a_row(self, player, row):
        return self.winning_rows(player, row) == 3
    
    def someone_won(self):
        for row in TTTGame.WINNING_COMBOS:
            if self.three_in_a_row(self.human, row):
                self.winner = 'Human'
                return True
            elif self.three_in_a_row(self.computer, row):
                self.winner = 'Computer'
                return True
        
        return False    
    
    def is_game_over(self):
        return self.board.is_full() or self.someone_won()
    
    def human_move(self):
        choice = None
        while True:
            valid_choices = self.board.empty_squares()
            choice = input(f'Choose a square in {valid_choices}: ')
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass
            
            print('Please enter a number between 1-9.')
            print()
        
        self.board.mark_square(choice, Square.HUMAN_MARKER)
    
    def computer_move(self):
        # Need to take out squares already taken
        valid_choices = self.board.empty_squares()
        choice = random.choice(valid_choices)
        self.board.mark_square(choice, Square.COMPUTER_MARKER)


game = TTTGame()
game.play()