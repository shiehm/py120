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

"""
Problem: For the PokerHand class we need 
1. to deal a hand with 5 cards 
2. to test if those 5 cards fit any combination 

Strategize 
- Can import the last 2 files to save space 


"""

class PokerHand:
    def __init__(self, deck):
        self._hand = [deck.draw() for _ in range(5)]
        self._str_hand = [str(card) for card in self._hand]
    
    def __str__(self):
        return f'{self._str_hand}'

    def print(self):
        print(self._str_hand)

    def rank_values(self):
        return [card.rank_value for card in self._hand]
    
    def suit_values(self):
        return [card.suit_value for card in self._hand]

    def _frequency(self):
        hand = self.rank_values()
        return [hand.count(hand[i]) for i in range(5)]

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"
    
    def _is_royal_flush(self):
        royal = all(rank >= 10 for rank in self.rank_values())
        return royal and self._is_flush() and self._is_straight()

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        return 4 in self._frequency()

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        suits = self.suit_values()
        return len(set(suits)) == 1

    def _is_straight(self):
        max_min = max(self.rank_values()) - min(self.rank_values()) == 4
        unique = len(set(self.rank_values())) == 5
        return max_min and unique

    def _is_three_of_a_kind(self):
        return 3 in self._frequency()

    def _is_two_pair(self):
        return self._frequency().count(2) == 4

    def _is_pair(self):
        return self._frequency().count(2) == 2
    

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")