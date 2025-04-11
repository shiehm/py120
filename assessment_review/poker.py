import random
import math

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


class PokerHand:
    def __init__(self, deck):
        self.hand = [deck.draw() for _ in range(5)]
        self.ranks = [Card.RANK_VALUES[card.rank] for card in self.hand]
        self.suits = [card.suit for card in self.hand]

    def print(self):
        print([str(card) for card in self.hand])
       
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
        return self._is_straight_flush() and sum(self.ranks) == 60

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_four_of_a_kind(self):
        for rank in self.ranks:
            if self.ranks.count(rank) == 4:
                return True
            return False
    
    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        unique = set(self.suits)
        return len(unique) == 1

    def _is_straight(self):
        all_unique = len(set(self.ranks)) == 5
        five_apart = max(self.ranks) - min(self.ranks) == 4
        return all_unique and five_apart

    def _is_three_of_a_kind(self):
        for rank in self.ranks:
            if self.ranks.count(rank) == 3:
                return True
        return False

    def _is_two_pair(self):
        unique = set(self.ranks)
        return len(unique) == 3

    def _is_pair(self):
        for rank in self.ranks:
            if self.ranks.count(rank) == 2:
                return True
    

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
print(hand.evaluate())

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
print(hand.evaluate())

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