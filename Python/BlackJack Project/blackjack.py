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
                self.all_cards.append(created_card)
                
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
        self.account += amount
        print("Your current balance is {}".format(self.account))
    
    def subtract_from_account(self, amount):
        self.account -= amount
        print("Your current balance is {}".format(self.account))
        
    def __str__(self):
        return self.name
        
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
    name = input("Please enter your name: ")
    player = Player(name)
    dealer = Dealer()
    deck = Deck()
    wager_amount = 0
    stillPlaying = True
    
    print("Welcome to Command Line Blackjack {}, there is a 5 minimum wager to start".format(player.name))
    
    while stillPlaying == True:
        if player.account > -100:
            print("You own too much money {}.".format(player.name))
            return
            
        while (int(wager_amount) < 5) and (isinstance(wager_amount, int)):

            try:
                wager_amount = int(input("How much would you like to bet ? "))
                deck.shuffle()
            except:
                print("Please enter an numeric amount higher then 5 ")

    
        dealer_cards = []
        player_cards = []

    # Starting the game with 2 cards each
        for _ in range(2):
            dealer_cards.append(deck.deal_one())
            player_cards.append(deck.deal_one())
    
        playerTotal = player_cards[0].value + player_cards[1].value
        dealerTotal = dealer_cards[0].value
        
        print("Dealers first card is a {} for a total of {} ".format(dealer_cards[0], dealerTotal))
        hit = input("{} cards are {} and {} for a total of {} do you want to hit ? ".format(player.name, player_cards[0], player_cards[1], playerTotal))
        while hit in ["Yes", "yes"]:

        
            player_cards.append(deck.deal_one())
            playerTotal += player_cards[-1].value
            if playerTotal > 21:
                print("{} has bust".format(player.name))
                player.subtract_from_account(wager_amount)
                wager_amount = 0
                hit = ""
            else:
                hit = input("Total is now {} hit ?".format(playerTotal))
                
        dealerTotal += dealer_cards[1].value
        print("Dealers total is {} ".format(dealerTotal))
        
        while dealerTotal <= 21:

            if dealerTotal > playerTotal:
                print("{} total is {}, the dealer wins ")
            else:
                dealer_cards.append(deck.deal_one())
                dealerTotal += dealer_cards[-1].value
                


    
start_game()
