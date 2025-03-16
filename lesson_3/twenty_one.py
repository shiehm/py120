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

Will just design a game for 2 players for now, 1 human and 1 computer dealer.

-- Nouns (objects)
-> Verbs (methods, behaviors)
-o Adjectives (variables, state)

Nouns/Verbs Extracted:
- Game 
    -> Determine Winner
        o Win
        o Lose
        o Tie
    -> Play
    -> Display Welcome / Goodbye Message
- Participants:
    - Dealer
    - Players
        -> Hit
        -> Stay
        -> Bet (can make automatic on first go)
        o Bust
        o Score
- Hand (Players have Hands)
    -> Reveal
    o Value (what the cards in a hand total to)
- Deck 
    -> Deal 
    -> Shuffle
- Cards (A deck has Cards)
    o Suits
    o Rank
"""

import random

class Participants:
    def __init__(self):
        self.hand = Hand()
    
    def hit(self, card):
        """
        Takes the top-most card from the deck -> Deck().deal()
        places it in the participant's hand -> Hand().add_card()
        """
        self.hand.add_card(card)
    
    def is_busted(self):
        return self.hand.get_value() > 21
    
    def score(self):
        pass

class Dealer(Participants):
    def __init__(self):
        super().__init__()
        
    def reveal(self):
        print(f'Dealer is showing: {self.hand.cards[0]}')

class Player(Participants):
    def __init__(self):
        super().__init__()

class Deck:
    SUITS = ['D', 'H', 'C', 'S']
    RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.shuffle_deck()
        
    def shuffle_deck(self):
        self.deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self.deck)
        
    def deal(self):
        if not self.deck:
            self.shuffle_deck()
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        cards = [card.rank for card in self.cards]
        value = 0
        
        for card in cards:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                value += 11
            else:
                value += int(card)
        
        aces = cards.count('A')
        while aces and value:
            value -= 10
            aces -= 1
        
        return value
    
    def __str__(self):
        return f'{[card for card in self.cards]}'
    
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class TwentyOneGame:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()
    
    def deal_cards(self):
        """
        This function will deal 1 card to a specific player
        """
        # This can be simplified later: 
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        
    def player_turn(self):
        print(f'Player Hand: {self.player.hand.cards}')
        self.dealer.reveal()
        
        while True:
            action = input('Hit or Stay? (type h or s): ')
            if action.casefold()[0] not in ['h', 's']:
                print('Invalid choice, please type hit or stay: ')
                action = input()
            
            if action == 'h':
                new_card = self.deck.deal()
                self.player.hit(new_card)
            
            if action == 's':
                break
        
    def dealer_turn(self):
        while self.dealer.hand.get_value() < 17:
            new_card = self.deck.deal()
            self.dealer.hit(new_card)
            if self.dealer.is_busted():
                break
        
    def display_result(self):
        # Need to work in what happens if busted, automatic win for the other player
        dealer_value = self.dealer.hand.get_value()
        player_value = self.player.hand.get_value()
        
        print(f'Dealer Hand: {self.dealer.hand}')
        print(f'Dealer Value: {dealer_value}')
        print()
        print(f'Player Hand: {self.player.hand}')
        print(f'Dealer Value: {player_value}')
        
        if self.player.is_busted():
            print('Player is busted')
        elif self.dealer.is_busted():
            print('Dealer is busted')
            
        if not self.player.is_busted() or self.dealer.is_busted():
            if player_value > dealer_value:
                print('Player Wins')
            elif player_value < dealer_value:
                print('Dealer Wins')
            else:
                print('It is a Tie')
        
    def display_welcome_message(self):
        print('Welcome to 21!')
        
    def display_goodbye_message(self):
        print('Thanks for playing!')
        
    def play(self):
        self.display_welcome_message()
        self.deal_cards()
        self.player_turn()
        self.dealer_turn()
        self.display_result()
        self.display_goodbye_message()
        
game = TwentyOneGame()
game.play()