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
        
        
cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]

print(min(cards) == Card(2, 'Hearts'))             # True
print(min(cards))

print(max(cards) == Card('Ace', 'Clubs'))          # True
print(max(cards))

print(str(min(cards)) == "2 of Hearts")            # True
print(str(min(cards)))

print(str(max(cards)) == "Ace of Clubs")           # True
print(str(max(cards)))


cards = [Card(5, 'Hearts')]

print(min(cards) == Card(5, 'Hearts'))             # True
print(min(cards))

print(max(cards) == Card(5, 'Hearts'))             # True
print(max(cards))

print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True
print(str(Card(5, 'Hearts')))


cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]

print(min(cards).rank == 4)                        # True
print(min(cards).rank)

print(max(cards) == Card(10, 'Clubs'))             # True
print(max(cards))

print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True
print(str(Card(10, 'Clubs')))


cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]

print(min(cards) == Card(7, 'Diamonds'))           # True
print(min(cards))

print(max(cards).rank == 'Jack')                   # True
print(max(cards).rank)

print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True
print(str(Card(7, 'Diamonds')))


cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]

print(min(cards).rank == 8)                        # True
print(min(cards).rank)

print(max(cards).rank == 8)                        # True
print(max(cards).rank)