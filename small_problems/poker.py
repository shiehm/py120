import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.rank_value + (self.suit_value/10)
    
    @property
    def rank_value(self):
        RANK = {x: x for x in range(2, 11)}
        RANK['Jack'] = 11
        RANK['Queen'] = 12
        RANK['King'] = 13
        RANK['Ace'] = 14
        
        return RANK[self.rank]
    
    @property
    def suit_value(self):
        SUIT = {
            'Diamonds': 1,
            'Clubs': 2,
            'Hearts': 3,
            'Spades': 4
        }
        
        return SUIT[self.suit]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    # Defining one of the comparisons, python can figure out the others
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.value > other.value
    
    # eq is explicitly needed so that python doesn't use 'is'
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.value == other.value 


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self._new_deck()
        
    def _new_deck(self):
        self._deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self._deck)
    
    def draw(self):
        if not self._deck:
            self._new_deck()
        
        return self._deck.pop()
        
    def __str__(self):
        return '\n'.join(str(card) for card in self._deck)

