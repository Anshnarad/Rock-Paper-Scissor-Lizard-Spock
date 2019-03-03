# GUI-based version of RPSLS
import simpleguitk as simplegui

print"\n \n"
print"************************ANSH NARAD************************"

print""

print"***************ROCK PAPER SCISSOR LIZARD SPOCK************"

print""

import random
pscore=0
cscore=0
outcome=""
def name_to_numb(name):


    if name=="rock":
        number=0
    elif name=="spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        print "error"
    return ""


def name_to_number(name):


    if name=="rock":
        number=0
    elif name=="spock":
        number=1
    elif name=="paper":
        number=2
    elif name=="lizard":
        number=3
    elif name=="scissors":
        number=4
    else:
        print "error"
    return number



def number_to_name(number):


    if number==0:
        name="rock"
    elif number==1:
        name="spock"
    elif number==2:
        name="paper"
    elif number==3:
        name="lizard"
    elif number==4:
        name="scissors"
    else:
        print "error"
    return name

# Functions that compute RPSLS

def rpsls(guess):
    global pscore,cscore
    print name_to_numb(guess)

    number=name_to_number(guess)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)

    print "Players choice : ", guess
    print "computer choice: ", comp_choice


    if (comp_number + 1) % 5 == number:
        print "Player wins!"
        pscore = pscore + 1
    elif (comp_number + 2) % 5 == number:
        print "Player wins!"
        pscore = pscore + 1
    elif comp_number == number :
        print "Player and computer tie!"
    else:
        print "Computer wins!"
        cscore = cscore + 1
    print ""


#function for each button

def rock():
    guess="rock"
    return get_guess(guess)

def paper():
    guess="paper"
    return get_guess(guess)

def scissor():
    guess="scissors"
    return get_guess(guess)

def lizard():
    guess="lizard"
    return get_guess(guess)

def spock():
    guess="spock"
    return get_guess(guess)

def end():
    global pscore,cscore,outcome

    if pscore > cscore:
        outcome = "Player wins!!"
    elif cscore > pscore:
        outcome = "Computer wins!!"
    else:
        outcome = "It's a Tie!!"

# Handler for input field

def get_guess(guess):

    if not (guess == "rock" or guess == "spock" or guess == "paper" or
            guess == "lizard" or guess == "scissors"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)


#draw handler

def draw(canvas):

    canvas.draw_text("ROCK PAPER SCISSOR LIZARD SPOCK",[50,25],22,"white")

    canvas.draw_text("Player score : %s" % pscore,[25,150],20,"white")

    canvas.draw_text("Computer score : %s" % cscore,[25,200],20,"white")

    canvas.draw_text("RESULT : %s" % outcome,[25,350],20,"yellow")
# Create frame and assign callbacks to event handlers

frame = simplegui.create_frame("GUI-based rpsls", 500, 500)

frame.add_button("Rock",rock,200)
frame.add_button("Paper",paper,200)
frame.add_button("Scissors",scissor,200)
frame.add_button("Lizard",lizard,200)
frame.add_button("Spock",spock,200)
frame.add_button("End",end,200)
frame.set_draw_handler(draw)
# Start the frame animation
frame.start()
