"""
Twenty-One:
The game is played with a standard playing card deck consisting of 52 cards, 
4 suits with 13 cards each from A, 2, 3.... 10, J, Q, K. The goal of the game 
is to get a hand that totals 21 without going over it (i.e. busting). There 
is a dealer and there can be multiple players (7 players max). Participants 
receive two cards. The dealer will hide one card and show the other card face 
up, while players know their own cards but don't have to show them. The players 
go first, choosing to hit or stay. A can count as 1 or 11 depending on the other 
cards in the hand (it will be 11 unless that causes the hand to bust, in which 
case it will be 1). If a player gets 21, that is the maximum and there is no 
other decision to be made. The players go first and the dealer goes last. If a 
player busts, they automatically lose and are out of the game. If the dealer 
busts the dealer is out and the players win. If the dealer has a hand that totals 
under 17, it must hit, otherwise if it is 17 or over, it must stay. The player 
with the highest hand value that is 21 or under wins. If multiple players / 
dealer has the same value, they tie. 

-- Nouns (objects)
-> Verbs (methods, behaviors)
-o Adjectives (variables, state)

Nouns/Verbs Extracted:
- Game 
    -> Determine Winner
    -> Win
    -> Lose
    -> Tie
- Participants:
    - Dealer
    - Players
        -> Hit
        -> Stay
- Hand (Players have Hands)
    -> Bust
    -> 21
    -> Reveal
    o Value (what the cards in a hand total to)
- Deck 
- Cards (A deck has Cards)
    o Suits
    o Rank
"""

class Participants:
    def __init__(self):
        pass

class Dealer(Participants):
    pass

class Player(Participants):
    def __init__(self):
        pass
    
    def hit(self):
        pass
    
    def stay(self):
        pass

class Hand:
    pass

class Deck:
    SUITS = ['D', 'H', 'C', 'S']
    RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    HIDDEN_CARD = ('X', 'X')
    
    def __init__(self):
        self.shuffle_deck()
        
    def shuffle_deck(self):
        self.deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # self.value = 
    
