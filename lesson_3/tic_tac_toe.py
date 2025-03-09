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

class Board:
    EMPTY = ' '
    PLAYER = 'X'
    COMPUTER = 'O'
    
    def __init__(self):
        self.squares = {
            1: Board.EMPTY,
            2: Board.EMPTY,
            3: Board.EMPTY,
            4: Board.EMPTY,
            5: Board.EMPTY,
            6: Board.EMPTY,
            7: Board.EMPTY,
            8: Board.EMPTY,
            9: Board.EMPTY
        }
    
    def display(self):
        line = '---+---+---'
        print()
        print(f' {self.squares[1]} | {self.squares[2]} | {self.squares[3]} ')
        print(line)
        print(f' {self.squares[4]} | {self.squares[5]} | {self.squares[6]} ')
        print(line)
        print(f' {self.squares[7]} | {self.squares[8]} | {self.squares[9]} ')

class Square:
    def __init__(self):
        pass

class Row:
    def __init__(self):
        pass

class Marker:
    def __init__(self):
        pass

class Player:
    def __init__(self):
        pass

    def mark(self):
        pass
    
    def play(self):
        pass

class Human(Player):
    def __init__(self):
        pass

class Computer(Player):
    def __init__(self):
        pass

# Orchestration Engine: a class that controls the flow of the app / part of the app
class TTTGame:
    def __init__(self):
        self.board = Board()

    def play(self):
        self.display_welcome_message()
        
        while True:
            self.first_player_move()
            
            if self.is_game_over():
                break
            
            self.second_player_move()
            if self.is_game_over():
                break
            
            # temporary program end 
            break
        
        self.board.display()
        self.display_results()
        self.display_goodbye_message()
    
    def display_results(self):
        # Stub
        pass
    
    def display_welcome_message(self):
        print('~Welcome~ to tic-tac-toe')
    
    def display_goodbye_message(self):
        print('~Thanks~ for playing tic-tac-toe!')
    
    def is_game_over(self):
        # Stub
        # if 3 in a row:
            # return True 
        return False
    
    def first_player_move(self):
        # Stub
        pass
    
    def second_player_move(self):
        # Stub
        pass


game = TTTGame()
game.play()