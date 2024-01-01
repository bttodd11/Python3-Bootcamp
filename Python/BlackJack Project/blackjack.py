import random
import os
import sys
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
        self.losses += add
        print("The dealers record is {} and {}".format(self.wins, self.losses))
        
def are_you_still_playing(stillPlaying):
    answer = ""
    answer = input("Would you like to play again ? ")
    clear_console()
    
    if answer == "Yes" or answer == "yes":
            return True
    else:
            sys.exit("Good game !")
    
def reset_user(type):
        if isinstance(type, str) == True:
            return ""
        else:
             return 0, 0, 0
    
def clear_console():
    os.system('clear')

# def show_stats():
    
    

def start_game():
    # Start of the game #
    name = input("Please enter your name: ")
    player = Player(name)
    dealer = Dealer()
    deck = Deck()
    wager_amount = 0
    stillPlaying = True
    hit = ""
    playerTotal = 0
    dealerTotal = 0
    print("Welcome to Command Line Blackjack {}, there is a 5 minimum wager to start".format(player.name))
    
    # While stillPlaying is true keep the gaming going
    while stillPlaying == True:

        if player.account < -100:
            print("You own too much money {}.".format(player.name))
            return
    # If wager amount is less than 5 and is a number, this is the start of a new game
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
        stillPlaying = False
        
        print("Dealers first card is a {} for a total of {} ".format(dealer_cards[0], dealerTotal))
        while hit not in ["Yes", "yes", "No", "no"]:
            try:
                hit = input("{} cards are {} and {} for a total of {} do you want to hit ? ".format(player.name, player_cards[0], player_cards[1], playerTotal))
            except:
                print("Invalid Response")
                
        # If the answer is No then need to run this.   
                print("Invalid Response")
                continue
        if hit in ["No", "no"]:
            dealerTotal += dealer_cards[-1].value
            print("Dealers next cards is a {} {}, the dealers total is now {}".format(dealer_cards[1].rank, dealer_cards[1].suit, dealerTotal))
            while dealerTotal <= 21:
                        
                if playerTotal > dealerTotal:
                    nextCard = deck.deal_one()
                    dealer_cards.append(nextCard)
                    dealerTotal += dealer_cards[-1].value
                    print("Dealers next card is a {} of {}, the dealers total is now {}".format(nextCard.rank, nextCard.suit, dealerTotal))
                    
                    if(dealerTotal > 21):
                         print("Dealer has bust, dealers total is {}".format(dealerTotal))
                         dealer.add_losses(1)
                         player.add_to_account(wager_amount)
                else:
                        
                    if dealerTotal <= 21 and dealerTotal > playerTotal:
                        print("Dealer wins, dealer's total is {}. {} total is {}".format(dealerTotal, player.name, playerTotal))
                        dealer.add_win(1)
                        player.subtract_from_account
                    else: 
                        print("{} wins, dealers total was {}".format(player.name, dealerTotal))
                        dealer.add_losses(1)
                        player.add_to_account(wager_amount)
                    break
                    
            stillPlaying = False
            playerTotal, dealerTotal, wager_amount = reset_user(playerTotal)
            stillPlaying = are_you_still_playing(stillPlaying)
            hit = reset_user(hit)
                        
               
            
        if hit in ["Yes", "yes"]:
            player_cards.append(deck.deal_one())
            playerTotal += player_cards[-1].value
            dealerTotal += dealer_cards[-1].value
            
            if playerTotal > 21:
                print("{} has bust, your total was {}, the dealers total was {} ".format(player.name, playerTotal, dealerTotal))
                dealer.add_win(1)
                player.subtract_from_account(wager_amount)
                
            else:
                print("Next card is a {} of {} for a total of {}".format(player_cards[-1].rank, player_cards[-1].suit, playerTotal))
                hit = reset_user(hit)
                hit = input("Total is now {} hit ? ".format(playerTotal))
                 
                while hit in ["Yes", "yes", "y"]:
                     player_cards.append(deck.deal_one())
                     playerTotal += player_cards[-1].value
                     print("Next card is a {} of {} for a total of {}".format(player_cards[-1].rank, player_cards[-1].suit, playerTotal))
                     
                     if playerTotal > 21:
                        print("{} has bust, your total was {}, the dealers total was {} ".format(player.name, playerTotal, dealerTotal))
                        player.subtract_from_account(wager_amount)
                        stillPlaying = False
                        stillPlaying = are_you_still_playing(stillPlaying)
                        playerTotal, dealerTotal, wager_amount = reset_user(playerTotal)
                        hit = reset_user(hit)
                        break
                        
                     hit = input("Total is now {} hit ? ".format(playerTotal))
                    
                
                while dealerTotal <= 21:
                    
                    if dealerTotal == 21:
                        print("Dealer has 21, dealer wins".format(player.name, playerTotal, dealerTotal))
                        player.subtract_from_account(wager_amount)
                        dealer.add_win(1)
                        break
                    elif dealerTotal > 21:
                        print("Dealer has bust, dealers total is {}".format(dealerTotal))
                        player.add_to_account(wager_amount)
                        dealer.add_losses(1)
                        break
                    elif dealerTotal == 21 and playerTotal == 21:
                        print("Both dealer and {} has 21, this game is void. ".format(player.name))
                        break
                    elif dealerTotal > playerTotal:
                         print("{}'s total is {}, the dealers total is {} the dealer wins".format(player.name, playerTotal, dealerTotal))
                         player.subtract_from_account(wager_amount)
                         dealer.add_win(1)
                         break    
                    else:
                        dealer_cards.append(deck.deal_one())
                        dealerTotal += dealer_cards[-1].value
                        
                        if dealerTotal > 21:
                            print("Dealer has bust, dealers total is {}".format(dealerTotal))
                            dealer.add_losses(1)
                            player.add_to_account(wager_amount)
                            
            
            # Once we break out of the while loop ask if we are going to play
            stillPlaying = False
            playerTotal, dealerTotal, wager_amount = reset_user(playerTotal)
            hit = reset_user(hit)
            stillPlaying = are_you_still_playing(stillPlaying)
            

                             
            
        
       

                


    
start_game()
