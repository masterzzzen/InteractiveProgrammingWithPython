# Guess the number

# To play this game, please visit this link: http://www.codeskulptor.org/#user29_usKkctLGuq_12.py
# and press the play button.

# HOW TO PLAY:
# First, select the range. 
# Then, enter a number into the console. 
# The program will tell you to guess a higher or lower number next time. 
# You have 10 chances. Enjoy!


import simplegui
import math
import random

# initialize global variables used in your code
secret_number = random.randrange(0, 100)
chances_left = math.ceil(math.log(100,2))

def init100():
    global secret_number
    secret_number = random.randrange(0, 100)
    global chances_left
    chances_left = math.ceil(math.log(100,2))
    print " "

def init1000():
    global secret_number
    secret_number = random.randrange(0, 1000)
    global chances_left
    chances_left = math.ceil(math.log(1000,2))
    print " "   
    
# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    print "New Game! The range is [0, 100)!!!"
    init100()    
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    print "New Game! The range is [0, 1000)!!!"
    init1000() 

                  
def get_input(guess):
    # main game logic goes here     
    global chances_left, secret_number  
    guessed = int(guess)

    if guessed > secret_number:
        chances_left -= 1
        if chances_left != 0:            
            print "Your guess was " + guess + "."
            print "You have %s chances left. Keep trying!" %(chances_left)
            print "Lower!"
            print " "
        else:
            print "GAME OVER...."
            print "New Game! The range is [0, 100) and you have 7 chances!"
            init100()  
            
    elif guessed < secret_number:
        chances_left -= 1
        if chances_left != 0:
            print "You guess was " + guess + "."
            print "You have %s chances left. Keep trying!" %(chances_left)
            print "Higher!"
            print " "
        else:
            print "GAME OVER...."
            print "New Game! The range is [0, 100) and you have 7 chances!"
            init100() 
    else:
            print "Your guess was " + guess + "."
            print "You win!"
            print " "            
            print "New Game! The range is [0, 100) and you have 7 chances!"
            print " "
            init100()
      
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 10000", range1000, 200) 
frame.add_input("Your input: ", get_input, 200)


# start frame
frame.start()


