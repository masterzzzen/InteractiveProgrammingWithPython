# Pong

# To play this game, please visit this link: http://www.codeskulptor.org/#user29_ieEcrAldJk_4.py
# and hit the play button to run the program
# HOW TO PLAY:
# To control the player on the left hand side, use "W"(up), "S"(down), "A"(left), and "D"(right)
# To control the player on the right hand side, use the regular arrow keys.


import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [300.0, 200.0] 
ball_vel = [0.0, 0.0]
paddle1_pos = [0.0 + HALF_PAD_WIDTH, 200.] 
paddle2_pos = [600.0 - HALF_PAD_WIDTH, 200.0]
paddle1_vel = [0.0, 0.0]
paddle2_vel = [0.0, 0.0]

score1 = 0
score2 = 0

paddle_touch = 0 
right = True
time = 0

'''point1_1 = [paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT]
point1_2 = [paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT]
point1_3 = [paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT]
point1_4 = [paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT]
point2_1 = [paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT]
point2_2 = [paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT]
point2_3 = [paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT]
point2_4 = [paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT]'''



# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos[0] = 300
    ball_pos[1] = 200
    '''ball_vel[0] = 2
    ball_vel[1] = -2
    '''
    choose_side = random.randrange(0,100)
    if choose_side >=50:
        right = True
    else:
        right = False   
        
    if right == True:
        ball_vel[0] = 1.5
        ball_vel[1] = -2
    else:
        ball_vel[0] = -1.5
        ball_vel[1] = -2

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    global right
    paddle1_pos[0] = 0 + HALF_PAD_WIDTH
    paddle1_pos[1] = 200 
    paddle2_pos[0] = 600 - HALF_PAD_WIDTH
    paddle2_pos[1] = 200 
    paddle1_vel[0] = 0
    paddle2_vel[1] = 0   
    paddle1_vel[0] = 0
    paddle2_vel[1] = 0  
    
    score1 = 0
    score2 = 0
    
    ball_init(right)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global point1_1, point1_2, point1_3, point1_4, point2_1, point2_2, point2_3, point2_4 
    # update paddle's vertical position, keep paddle on the screen

    paddle1_pos[0] = paddle1_pos[0] + paddle1_vel[0]
    paddle1_pos[1] = paddle1_pos[1] + paddle1_vel[1]    
    paddle2_pos[0] = paddle2_pos[0] + paddle2_vel[0]
    paddle2_pos[1] = paddle2_pos[1] + paddle2_vel[1]    

    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    # first, compute the 4 points of each paddle, none of the code crosses multiple lines   
    point1_1 = [paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT]
    point1_2 = [paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]-HALF_PAD_HEIGHT]
    point1_3 = [paddle1_pos[0]+HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT]
    point1_4 = [paddle1_pos[0]-HALF_PAD_WIDTH, paddle1_pos[1]+HALF_PAD_HEIGHT]
    point2_1 = [paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT]
    point2_2 = [paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]-HALF_PAD_HEIGHT]
    point2_3 = [paddle2_pos[0]+HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT]
    point2_4 = [paddle2_pos[0]-HALF_PAD_WIDTH, paddle2_pos[1]+HALF_PAD_HEIGHT]
    
    c.draw_polygon([(point1_1[0], point1_1[1]), (point1_2[0], point1_2[1]), (point1_3[0], point1_3[1]), (point1_4[0], point1_4[1])], 0.01, "White", "White")
    c.draw_polygon([(point2_1[0], point2_1[1]), (point2_2[0], point2_2[1]), (point2_3[0], point2_3[1]), (point2_4[0], point2_4[1])], 0.01, "White", "White")
    
    # update ball
    ball_top = [ball_pos[0], ball_pos[1] - BALL_RADIUS]
    ball_bottom = [ball_pos[0], ball_pos[1] + BALL_RADIUS]
    ball_left = [ball_pos[0] - BALL_RADIUS, ball_pos[1]]
    ball_right = [ball_pos[0] + BALL_RADIUS, ball_pos[1]]
    
    if ball_top[1] == 0:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = - ball_vel[1]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    elif ball_bottom[1] == 400:
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = - ball_vel[1]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    elif ball_left[0] <= point1_2[0] and ball_left[1] >= point1_2[1] and ball_left[1] <= point1_3[1]:
        ball_vel[0] = -ball_vel[0]
        ball_vel[1] = ball_vel[1]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    elif ball_right[0] >= point2_1[0] and ball_left[1] >= point2_1[1] and ball_left[1] <= point2_4[1]:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = ball_vel[1]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    elif ball_left[0] <= 8:
        score2 += 1
        ball_init(right) 
    elif ball_right[0] >= 592:
        score1 += 1
        ball_init(right)         
    else: 
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]

    
    # draw ball and scores
    c.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 0.1, "White", "White")
    c.draw_text(str(score1),[50,50], 20, "White") 
    c.draw_text(str(score2),[545,50], 20, "White")
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    acceleration = 5
 
    '''if paddle1_pos[1]- HALF_PAD_HEIGHT <= 0 and paddle1_pos[1]+ HALF_PAD_HEIGHT >= 400:
        paddle1_vel[1] = 0
    else: 
        if key == simplegui.KEY_MAP["w"]:
            paddle1_vel[1] -= acceleration         
        elif key == simplegui.KEY_MAP["s"]:
            paddle1_vel[1] += acceleration 
        
    if paddle2_pos[1]-HALF_PAD_HEIGHT > 0.0 and paddle2_pos[1]+ HALF_PAD_HEIGHT < 400.0:
        if key == simplegui.KEY_MAP["up"]:
            paddle2_vel[1] -= acceleration        
        elif key == simplegui.KEY_MAP["down"]:
            paddle2_vel[1] += acceleration
    else: 
        paddle2_vel[1] = 0'''

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= acceleration         
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] += acceleration
        
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= acceleration        
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += acceleration
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0       
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0    
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0 
      
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 150)

# start frame
new_game() 
frame.start()
