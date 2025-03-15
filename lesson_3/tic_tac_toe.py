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
        self.reset()
    
    def reset(self):
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
        self.score = 0
    
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
            (1, 2, 3), # Horizontal
            (4, 5, 6), # Horizontal
            (7, 8, 9), # Horizontal
            (1, 5, 9), # Diagonal
            (3, 5, 7), # Diagonal
            (1, 4, 7), # Vertical
            (2, 5, 8), # Vertical
            (3, 6, 9)  # Vertical
            )
    
    @staticmethod
    def _join_or(lst, separator=', ', conjunction='or'):
        if len(lst) > 1:
            new_lst = [str(num) for num in lst]
            new_lst[-1] = f'{conjunction} {lst[-1]}'
            return separator.join(new_lst)
        else:
            return lst[0]
    
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.winner = None
        self.pick_first_player()
    
    def pick_first_player(self):
        first = input('Who goes first? (Computer or Human?): ')
        while first[0].casefold() not in ['c', 'h']:
            print('Please enter C for computer or H for human: ')
            first = input()
        
        if first.startswith('c'):
            self.current_player = self.computer
        elif first.startswith('h'):
            self.current_player = self.human
    
    def toggle_player(self):
        if self.current_player == self.human:
            self.current_player = self.computer
        else:
            self.current_player = self.human
    
    def player_moves(self, player):
        if player == self.human:
            self.human_move()
        elif player == self.computer:
            self.computer_move()
    
    def play_again(self):
        again = input('Play again? (y/n): ')
        while again[0].casefold() not in ['y', 'n']:
            print('Please enter yes or no (y/n): ')
            again = input()
        return again.startswith('y')
    
    def play_once(self):
        self.board.reset()
        self.winner = None
        while True:
            self.board.display()
            self.player_moves(self.current_player)
            if self.is_game_over():
                break
            self.toggle_player()
        
        self.board.display()
        self.display_results()
        
    def play(self):
        self.display_welcome_message()
        
        play_again = True
        while play_again:
            self.play_once()
            play_again = self.play_again()
            self.toggle_player()
            
        self.display_goodbye_message()
    
    def display_results(self):
        if self.winner:
            print(f'The winner is {self.winner}!')
        else:
            print('It is a Tie!')
        
        print(f'Human Wins: {self.human.score}')
        print(f'Computer Wins: {self.computer.score}')
    
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
        
    def two_in_a_row(self, player, row):
        return self.winning_rows(player, row) == 2
    
    def identify_winning_move(self, player):
        for row in TTTGame.WINNING_COMBOS:
            if self.two_in_a_row(player, row):
                for key in row:
                    if key in self.board.empty_squares():
                        return key
    
    def someone_won(self):
        for row in TTTGame.WINNING_COMBOS:
            if self.three_in_a_row(self.human, row):
                self.winner = 'Human'
                self.human.score += 1
                return True
            elif self.three_in_a_row(self.computer, row):
                self.winner = 'Computer'
                self.computer.score += 1
                return True
        
        return False    
    
    def is_game_over(self):
        return self.board.is_full() or self.someone_won()
    
    def human_move(self):
        choice = None
        while True:
            valid_choices = self.board.empty_squares()
            choice = input(f'Choose a square in {TTTGame._join_or(valid_choices)}: ')
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
        valid_choices = self.board.empty_squares()
        
        if self.identify_winning_move(self.computer):
            choice = self.identify_winning_move(self.computer)
            print('Computer is going offensive!')
        elif self.identify_winning_move(self.human):
            choice = self.identify_winning_move(self.human)
            print('Computer is going defensive!')
        elif 5 in valid_choices:
            choice = 5
            print('Computer is taking the middle square!')
        else:
            choice = random.choice(valid_choices)
            print('Computer is choosing randomly!')
        
        self.board.mark_square(choice, Square.COMPUTER_MARKER)

game = TTTGame()
game.play()