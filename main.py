import pygame, sys, time, random
from pygame.locals import *
import time


size=[500,500]
pygame.init()
screen=pygame.display.set_mode(size)

# Colors
LIME = (0,255,0)
RED = (255, 0, 0)
BLACK = (0,0,0)
LIGHT_BLUE = (47,208,240)
SALMON = (255,192,203)
WHITE = (255,255,255)
LIGHT_GREEN = (90, 228, 32)
SKY_BLUE = (176, 226, 255)
PURPLE = (153,51,255)
ORANGE = (255,128,0)
YELLOW = (255,255,102)
screen.fill(BLACK)

# Width and Height of game box
width=50
height=50

# Margin between each cell
margin = 5

grid=[0]


#keeps track of selection 1 and 2
selection = 0

# Set title of screen
pygame.display.set_caption("Memory Game")

#Keeps game going until done
done=False
backcard = []
card1_1 = SKY_BLUE
backcard.append(card1_1)
card2_2 = SKY_BLUE
backcard.append(card2_2)
card3_3 = SKY_BLUE
backcard.append(card3_3)
card4_4 = SKY_BLUE
backcard.append(card4_4)
card5_5 = SKY_BLUE
backcard.append(card5_5)
card6_6 = SKY_BLUE
backcard.append(card6_6)
card7_7 = SKY_BLUE
backcard.append(card7_7)
card8_8 = SKY_BLUE
backcard.append(card8_8)
backcard = backcard * 2
# Used to manage how fast the screen updates
clock=pygame.time.Clock()

cards = []
card1 = RED
cards.append(card1)
card2 = LIME
cards.append(card2)
card3 = LIGHT_BLUE
cards.append(card3)
card4 = SALMON
cards.append(card4)
card5 = LIGHT_GREEN
cards.append(card5)
card6 = ORANGE
cards.append(card6)
card7 = PURPLE
cards.append(card7)
card8 = YELLOW
cards.append(card8)
cards = cards * 2
random.shuffle(cards)
#make board smaller, and dup the cards list
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
        # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
            column=pos[0] // (width+margin)
            row=pos[1] // (height+margin)
            print(pos,"Grid coordinates: ",row,column)
    back_cardposition = 0
    card_position = 0
    # Draw the grid
    for row in range(4):
        for column in range(4):
            pygame.draw.rect(screen,cards[card_position],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
            card_position = card_position + 1
    for row in range(4):
        for column in range(4):
            pygame.draw.rect(screen,backcard[back_cardposition],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
            back_cardposition = back_cardposition + 1
    if event.type == pygame.MOUSEBUTTONDOWN:
        column=pos[0] // (width+margin)
        row=pos[1] // (height+margin)
        if row == 0 and column == 0:
            pygame.draw.rect(screen,cards[0],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
        if row == 0 and column == 1:
            pygame.draw.rect(screen,cards[1],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
        if row == 0 and column == 2:
            pygame.draw.rect(screen,cards[2],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
        if row == 0 and column == 3:
            pygame.draw.rect(screen,cards[3],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])

    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
