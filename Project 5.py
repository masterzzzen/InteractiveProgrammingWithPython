# Blackjack

# To play this game, please visit this link: http://www.codeskulptor.org/#user29_ieEcrAldJk_6.py
# and hit the play button to run the program

# HOW TO PLAY:
# To view playing rules for the game of BlackJack, please visit: http://en.wikipedia.org/wiki/Blackjack 


import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
wins = 0
losses = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []            

    def __str__(self):
        cards = ''
        for card in self.hand:
            cards += str(card) + " "
        return cards        
    
    def add_card(self, card):
        self.hand.append(card) 

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0        
        ace_count = 0
        for card in self.hand:
            value += VALUES[card.get_rank()]        
            if card.get_rank() == "A": 
                ace_count += 1
        
        if ace_count > 0 and (value + 10) <= 21:
            value += 10        
        return value
 
    def draw(self, canvas, pos, in_play):
        # draw a hand on the canvas, use the draw method for cards        
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, [pos[0] + (i+1)*80, pos[1]])                
        if in_play == True:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,[pos[0] + CARD_BACK_CENTER[0] + 80, pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE) 
 
    
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append((Card(suit, rank)))
        random.shuffle(self.deck)        
        
    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        random.shuffle(self.deck)        
                       
    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(0) 
            
    def __str__(self):
        # return a string representing the deck
        current_deck = " "
        for card in self.deck:
            current_deck += str(card) + ", "
        return current_deck 
            



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, wins, losses
    
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    # your code goes here      
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    outcome = "Hit or Stand?"
    
    if in_play == True:
        losses += 1
    
    in_play = True    

    
def hit():
    global in_play, player_hand, outcome, wins, losses
    # replace with your code below
    value = player_hand.get_value()
    #print value
    # if the hand is in play, hit the player
    if in_play == True: 
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You have busted. New Deal?"
            in_play = False
            losses += 1   
    # if busted, assign a message to outcome, update in_play and score

    
def stand():
    global in_play, outcome, wins, losses
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            wins += 1
            outcome = "You Win! Nwe Deal?"
            in_play = False
        elif dealer_hand.get_value() >= player_hand.get_value():
            losses += 1
            outcome = "You Lose. New Deal?"
            in_play = False
        else:
            wins += 1
            outcome = "You Win! New Deal?"
            in_play = False


# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    dealer_hand.draw(canvas, [0, 100], in_play)
    player_hand.draw(canvas, [0, 300], False)          
    canvas.draw_text("Blackjack", [320, 250], 40, "White")
    #text output
    canvas.draw_text("Dealer", [10, 125], 20, "White")
    canvas.draw_text("Player", [10, 325], 20, "White")
    canvas.draw_text(outcome, [60, 250], 20, "White")
    canvas.draw_text("Wins: " + str(wins), [400, 50], 20, "Yellow")
    canvas.draw_text("Losses: " + str(losses), [400, 80], 20, "Yellow")
    
#initial hand and deck
deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
    
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
