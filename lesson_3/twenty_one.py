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
        self.reset()
    
    def hit(self, card):
        self.hand.add_card(card)
    
    def is_busted(self):
        return self.hand.get_value() > 21
    
    def reset(self):
        self.hand = Hand()

class Dealer(Participants):
    def __init__(self):
        super().__init__()

class Player(Participants):
    def __init__(self):
        super().__init__()
        self.bankroll = 500

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
        while aces and value > 21:
            value -= 10
            aces -= 1
        
        return value
    
    def __str__(self):
        return f'{[str(card) for card in self.cards]}'

class Deck:
    SUITS = ['D', 'H', 'C', 'S']
    RANKS = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
    
    def __init__(self):
        self.shuffle()
        
    def shuffle(self):
        self.deck = [Card(rank, suit) for suit in Deck.SUITS for rank in Deck.RANKS]
        random.shuffle(self.deck)
        
    def deal(self):
        if not self.deck:
            self.shuffle()
        return self.deck.pop()
    
    def deal_hidden(self):
        if not self.deck:
            self.shuffle()
        card = self.deck.pop()
        card.hide()
        return card
    
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self._hidden = False
    
    def hide(self):
        self._hidden = True
    
    def reveal(self):
        self._hidden = False
    
    def __str__(self):
        if self._hidden == True:
            return 'X of X'
        return f'{self.rank} of {self.suit}'
    
class TwentyOneGame:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()
        self.winner = None
    
    def deal_cards(self):
        self.dealer.hand.add_card(self.deck.deal_hidden())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
    
    def player_turn(self):
        while True:
            print()
            print(f'Player Hand: {self.player.hand}')
            print(f'Dealer Hand: {self.dealer.hand}')
            
            action = input('Hit or Stay? (type h or s): ')
            if action.casefold()[0] not in ['h', 's']:
                action = input('Invalid choice, please type hit or stay: ')
            
            if action.casefold()[0] == 'h':
                new_card = self.deck.deal()
                self.player.hit(new_card)
            else:
                break
            
            if self.player.is_busted():
                print('Player is busted')
                self.winner = self.dealer
                break
        
    def dealer_turn(self):
        while self.dealer.hand.get_value() < 17:
            new_card = self.deck.deal()
            self.dealer.hit(new_card)
            
            if self.dealer.is_busted():
                print('Dealer is busted')
                self.winner = self.player
                break
    
    def display_result(self):
        # Need to work in what happens if busted, automatic win for the other player
        self.dealer.hand.cards[0].reveal()
        dealer_value = self.dealer.hand.get_value()
        player_value = self.player.hand.get_value()
        
        print()
        print(f'Dealer Hand: {self.dealer.hand}')
        print(f'Dealer Value: {dealer_value}')
        print(f'Player Hand: {self.player.hand}')
        print(f'Player Value: {player_value}')
            
        if not self.player.is_busted() and not self.dealer.is_busted():
            if player_value > dealer_value:
                print('Player Wins')
                self.winner = self.player
            elif player_value < dealer_value:
                print('Dealer Wins')
                self.winner = self.dealer
            else:
                print('It is a Tie')
    
    def settle_bets(self):
        if self.winner == self.player:
            self.player.bankroll += self.bet
        if self.winner == self.dealer:
            self.player.bankroll -= self.bet
    
    def display_welcome_message(self):
        print('Welcome to 21!')
        
    def display_goodbye_message(self):
        print('Thanks for playing!')
        
    def set_bet(self):
        max_bet = self.player.bankroll
        print(f'Your bankroll is {max_bet}.')
        
        while True:
            bet = input('How much would you like to bet? ')
            try:
                bet = int(bet)
            except:
                print('Please enter an integer')
                    
            if bet > 1 and bet <= max_bet:
                self.bet = bet
                break
            
            print(f'Please enter an integer between 1 and {max_bet}')
    
    def reset(self):
        self.deck.shuffle()
        self.player.reset()
        self.dealer.reset()
        self.bet = 0
        self.winner = None
    
    def play_again(self):
        again = input('Play Again? (y/n): ')
        if again.casefold()[0] not in ['y', 'n']:
            again = input('Invalid response, enter y/n: ')
            
        if again.casefold()[0] == 'n':
            return False
        return True
    
    def play(self):
        self.display_welcome_message()
        
        while True:
            self.reset()
            self.set_bet()
            self.deal_cards()
            
            self.player_turn()
            if not self.player.is_busted():
                self.dealer_turn()
            
            self.display_result()
            self.settle_bets()
            
            if not self.play_again():
                break
            
            if self.player.bankroll == 0:
                print('You are out of money!')
                break
            
        self.display_goodbye_message()
        
game = TwentyOneGame()
game.play()