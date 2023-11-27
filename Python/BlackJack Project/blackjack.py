import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 10 }

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
    
class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_card.append(created_card)
                
    def shuffle(self):
        print("Shuffling ....")
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
    
class Player:
    def __init__(self, name):
        self.name = name
        self.account = 100
        
    def check_wager(self, amount):
        if amount > self.account:
            print("You do not have enough funds left in your account, please change you wager or add more money")
            return False
        else:
            return True
        
    def add_to_account(self, amount):
        self_account += amount
        print("Your current balance is {}".format(self_account))
    
    def subtract_from_account(self, amount):
        self_account -= amount
        print("Your current balance is {}".format(self_account))
        
class Dealer:
    def __init__(self, name = "Dealer"):
        self.name = name
        self.wins = 0
        self.losses = 0
        
    def add_win(self, add):
        self.wins += add
        print("The dealers record is {} and {}".format(self.wins, self.losses))
        
    def add_losses(self, add):
        self.wins += add
        print("The dealers record is {} and {}".format(self.wins, self.losses))
    

def start_game():
# Start of the game #
    name = print(input("Please enter your name"))
    player = Player(name)
    dealer = Dealer()
    deck = Deck()
    wager_amount = 0
    
    
    print("Welcome to Command Line Blackjack {}, there is a 5 minimum wager to start".format(player.name))
    
    while wager_amount < 5 and wager_amount.isDigit():
        wager_amount = int(input("How much would you like to bet ?"))
        
    
    dealer_cards = []
    player_cards = []
    
    # Starting the game with 2 cards each
    for _ in range(2):
        dealer_cards.append(deck.deal_one())
        player_cards.append(deck.deal_one())
        


    
    
