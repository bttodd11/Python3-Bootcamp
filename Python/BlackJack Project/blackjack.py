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
    deck = Deck()
    wager_amount = 0
    stillPlaying = True
    hit = ""
    
    print("Welcome to Command Line Blackjack {}, there is a 5 minimum wager to start".format(player.name))
    
    
    while stillPlaying == True:
        hit = ""
        if player.account < -100:
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
        while hit not in ["Yes", "yes", "y", "Y"]:
            try:
                hit = input("{} cards are {} and {} for a total of {} do you want to hit ? ".format(player.name, player_cards[0], player_cards[1], playerTotal))
            except:    
                print("Invalid Response")
                continue
            else:
                if hit in ["No", "n", "no"]:
                    dealerTotal += dealer_cards[1].value
                    print("Dealers next cards is a {} {}, the dealers total is now {}".format(dealer_cards[1].rank, dealer_cards[1].suit, dealerTotal))
                    while dealerTotal < 21:
                        
                        if playerTotal > dealerTotal:
                            nextCard = deck.deal_one()
                            
                            print("Dealers next card is a {} of {}".format(nextCard.rank, nextCard.suit))
                            dealerTotal += nextCard.value
                        else:
                            break
                        
                    if dealerTotal > playerTotal:
                        print("Dealer wins, dealer's total is {}. {} total is {}".format(dealerTotal, player.name, playerTotal))
                    else: 
                        print("{} wins, dealers total was {}".format(player.name, dealerTotal))  

                    stillPlaying = False
                    answer = input("Would you like to play again ? ")
                    
                    if answer == "Yes" or "yes":
                        dealerTotal = 0
                        playerTotal = 0
                        wager_amount = 0
                        stillPlaying = True
                    else: 
                        return
                            
            
        player_cards.append(deck.deal_one())
        playerTotal += player_cards[-1].value
        if playerTotal > 21:
            print("{} has bust, your total was {}, the dealers total was {} ".format(player.name, playerTotal, dealerTotal))
            player.subtract_from_account(wager_amount)
            wager_amount = 0
            stillPlaying = False
            answer = input("Would you like to play again ? ")
                
            if answer == "Yes" or "yes":
                dealerTotal = 0
                playerTotal = 0
                hit = ""
                wager_amount = 0
                stillPlaying = True
            else: 
                return
                
        else:
            hit = input("Total is now {} hit ? ".format(playerTotal))
                
            dealerTotal += dealer_cards[1].value
        
            while dealerTotal <= 21:

                if dealerTotal > playerTotal:
                    print("{}'s total is {}, the dealers total is {} the dealer wins".format(player.name, playerTotal, dealerTotal))
                    stillPlaying = False
                    answer = input("Would you like to play again ? ")
                
                    if answer == "Yes" or "yes":
                        dealerTotal = 0
                        playerTotal = 0
                        hit = ""
                        wager_amount = 0
                        stillPlaying = True
                    else: 
                        return
                    
                else:
                    dealer_cards.append(deck.deal_one())
                    dealerTotal += dealer_cards[-1].value
                    

                


    
start_game()
