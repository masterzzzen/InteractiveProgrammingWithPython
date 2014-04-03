# Stopwatch: The Game

# To play this game, please visit this link: http://www.codeskulptor.org/#user29_Kmlnr7EbMN_3.py
# and press the play button.

# HOW TO PLAY:
# In this game, you try to stop the watch on the full second. Score is measured by how many times 
# you succeeded vs. how many times you played. 


import simplegui
import math


# define global variables
successes = 0
tries = 0
timer_running = False
time_now = "0:00.0"
t = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    global time_now
    tenth_seconds = t%10
    minutes = math.floor(t/600)
    seconds = math.floor((t-minutes*600)/10)
    if seconds < 10:
        time_now = str(minutes) + ":" + "0" + str(seconds) + "." + str(tenth_seconds)
    else:
        time_now = str(minutes) + ":" + str(seconds) + "." + str(tenth_seconds)
    return time_now    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_running
    timer_running = True
    timer.start()

    
def stop():
    global timer_running, successes, tries
    timer.stop()
    if timer_running == True:
        tries += 1
    if t%10 == 0 and t !=0:
        successes += 1
    timer_running = False
    

def reset():
    global t, timer_running, successes, tries
    t = 0
    timer_running = False
    successes = 0
    tries = 0
    format(t)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    format(t)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(str(successes)+"/"+str(tries),[250,20],20, "Blue")
    canvas.draw_text(time_now, [80,120],40,"Blue")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 300, 180)
timer = simplegui.create_timer(100, timer_handler)
# register event handlers
frame.set_draw_handler(draw)
start_button = frame.add_button("Start", start, 100)
stop_button = frame.add_button("Stop", stop, 100)
reset_button = frame.add_button("Reset", reset, 100)



# start frame
frame.start()

