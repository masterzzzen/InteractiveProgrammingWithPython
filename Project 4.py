# Memory Card Game

# To play this game, please visit this link: http://www.codeskulptor.org/#user29_gIAuKCRq2N_4.py
# and hit the play button to run the program

# HOW TO PLAY:
# There are 8 pairs of cards on the table and each pair is identical
# At the beginning, all of the cards are flipped faced-down. 
# By clicking on a card, you flip it faced-up and then in your next selection
# you try to find the other card in the identical pair
# If your choice is correct, both cards stay flipped faced-up and if your
# choice is incorrect, both cards become flipped faced-down again.
# Your score is the total number of moves you make to find all of the identical pairs.
# So, really use your memory!


import simplegui
import random
count = 0
deck = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
recent = []
exposed = 0
corrects = 0

# helper function to initialize globals
def init():
    global deck, count, recent, exposed, corrects
    count = 0
    deck = []
    recent = []
    exposed = 0
    corrects = 0
    numbers = [x % 8 for x in range(16)]
    random.shuffle(numbers)
    for i in range(16):
        deck.append([50 * i, numbers[i], False, False])
 
def face_all_down():
    for i in deck:
        if not i[3]: 
            i[2] = False

     
# define event handlers
def mouseclick(pos):
    global exposed, recent, count, corrects
    x, y = pos
    if exposed == False:
        for card in deck:
            if 0 < (x - card[0]) < 50:
                 if not card[2]:
                    card[2] = True
                    recent = card
                    exposed = 1
                    count += 1
    elif exposed == True:
        for card in deck:
            if 0 < (x - card[0]) < 50:
                 if not card[2]:
                    card[2] = True
                    exposed = 2
                    if recent[1] == card[1]:
                        recent[3] = True
                        card[3] = True
                        corrects += 1
                    count += 1
    else:
        for card in deck:
            if 0 < (x - card[0]) < 50:
                 if not card[2]:
                    face_all_down()
                    card[2] = True
                    recent = card
                    exposed = 1
                    count += 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in deck:
        label.set_text("Moves = " + str(count // 2))
        if i[2]:
            canvas.draw_text(str(i[1]), 
                         (i[0] + 10, 100 - 30), 
                         70, "Yellow")
        else:
            canvas.draw_polygon([(i[0], 0),(i[0] + 50, 0),(i[0] + 50, 100), (i[0], 100)], 1, "Red", "Green")
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
