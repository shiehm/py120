import random

class Deck:
    def __init__(self):
        self._shuffle()
    
    def _shuffle(self):
        self._deck = [Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS]
        random.shuffle(self._deck)
    
    def draw(self):
        if not self._deck:
            self._shuffle()
        return self._deck.pop()

class Card:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    RANK_VALUES = {rank: num for rank, num in zip(RANKS, range(2, 15))}
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

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value == other.value


deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).