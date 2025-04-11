class Card:
    RANKS = ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    RANK_VALUES = {suit: num for suit, num in zip(RANKS, range(11, 15))}
    SUIT_VALUES = {suit: num/10 for suit, num in zip(SUITS, range(1, 5))}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property
    def value(self):
        return Card.RANK_VALUES.get(self.rank, self.rank) + Card.SUIT_VALUES[self.suit]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value
    
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value > other.value

    def __le__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value <= other.value

    def __ge__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value >= other.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value == other.value

    def __ne__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value != other.value

cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True