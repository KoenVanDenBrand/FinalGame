import pygame, sys, time, random
from pygame.locals import *
import time


size=[225,300]
pygame.init()
screen=pygame.display.set_mode(size)

BASICFONT = pygame.font.Font('freesansbold.ttf', 30)
Surf = BASICFONT.render("YOU WON!", 1, (255,255,255))
# Colors
GRAY = (0,255,0)
RED = (255, 0, 0)
BLACK = (0,0,0)
LIGHT_BLUE = (47,208,240)
SALMON = (255,192,203)
WHITE = (255,255,255)
LIGHT_GREEN = (160, 160, 160)
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

match = 0

#keeps track of selection 1 and 2
selection1 = False
selection2 = False

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

color1 = 0
color2 = 1
value1 = 0
value2 = 0

cards = []
card1 = RED
cards.append(card1)
card2 = GRAY
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

Menu = True
#make board smaller, and dup the cards list
while done==False:
    while Menu == True:
            screen.fill(BLACK)
            myfont=pygame.font.SysFont("Britannic Bold", 20)
            startlabel=myfont.render("WELCOME TO MEMORY", 1, (255, 255, 255))
            startlabel4 = myfont.render("Press [SPACEBAR] to start", 1, (255, 255, 255))
            startlabel2 = myfont.render("You have to find 8 matches", 1,(255,255,255,))
            startlabel3 = myfont.render("Click boxes to reveal it's color!", 1,(255,255,255))
            screen.blit(startlabel,(38,70))
            screen.blit(startlabel2,(32,100))
            screen.blit(startlabel3,(23,120))
            screen.blit(startlabel4,(31,160))
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key == K_SPACE:
                        Menu = False
                        screen.fill(BLACK)
            pygame.display.flip()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column=pos[0] // (width+margin)
            row=pos[1] // (height+margin)

            if row == 0 and column == 0:
                backcard[0] = cards[0]
                pygame.draw.rect(screen,backcard[0],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 = cards[0]
                    value1 = 0
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 = cards[0]
                    value2 = 0

            if row == 0 and column == 1:
                backcard[1] = cards[1]
                pygame.draw.rect(screen,backcard[1],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 = cards[1]
                    value1 = 1
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 = cards[1]
                    value2 = 1

            if row == 0 and column == 2:
                backcard[2] = cards[2]
                pygame.draw.rect(screen,backcard[2],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[2]
                    value1 = 2
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[2]
                    value2 = 2
            if row == 0 and column == 3:
                backcard[3] = cards[3]
                pygame.draw.rect(screen,backcard[3],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[3]
                    value1 = 3
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[3]
                    value2 = 3

            if row == 1 and column == 0:
                backcard[4] = cards[4]
                pygame.draw.rect(screen,backcard[4],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[4]
                    value1 = 4
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[4]
                    value2 = 4

            if row == 1 and column == 1:
                backcard[5] = cards[5]
                pygame.draw.rect(screen,backcard[5],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[5]
                    value1 = 5
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[5]
                    value2 = 5

            if row == 1 and column == 2:
                backcard[6] = cards[6]
                pygame.draw.rect(screen,backcard[6],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[6]
                    value1 = 6
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[6]
                    value2 = 6

            if row == 1 and column == 3:
                backcard[7] = cards[7]
                pygame.draw.rect(screen,backcard[7],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[7]
                    value1 = 7
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[7]
                    value2 = 7

            if row == 2 and column == 0:
                backcard[8] = cards[8]
                pygame.draw.rect(screen,backcard[8],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[8]
                    value1 = 8
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[8]
                    value2 = 8

            if row == 2 and column == 1:
                backcard[9] = cards[9]
                pygame.draw.rect(screen,backcard[9],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[9]
                    value1 = 9
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[9]
                    value2 = 9

            if row == 2 and column == 2:
                backcard[10] = cards[10]
                pygame.draw.rect(screen,backcard[10],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[10]
                    value1 = 10
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[10]
                    value2 = 10

            if row == 2 and column == 3:
                backcard[11] = cards[11]
                pygame.draw.rect(screen,backcard[11],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[11]
                    value1 = 11
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[11]
                    value1 == 11

            if row == 3 and column == 0:
                backcard[12] = cards[12]
                pygame.draw.rect(screen,backcard[12],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[12]
                    value1 = 12
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[12]
                    value2 = 12

            if row == 3 and column == 1:
                backcard[13] = cards[13]
                pygame.draw.rect(screen,backcard[13],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[13]
                    value1 = 13
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[13]
                    value2 = 13

            if row == 3 and column == 2:
                backcard[14] = cards[14]
                pygame.draw.rect(screen,backcard[14],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 =cards[14]
                    value1 = 14
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 =cards[14]
                    value2 = 14

            if row == 3 and column == 3:
                backcard[15] = cards[15]
                pygame.draw.rect(screen,backcard[15],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
                if selection1 == False:
                    selection1 = True
                    color1 = cards[15]
                    value1 = 15
                elif selection1 == True and selection2 == False:
                    selection2 = True
                    color2 = cards[15]
                    value2 = 15

    back_cardposition = 0
    card_position = 0
    # Draw the grid
    for row in range(4):
        for column in range(4):
            pygame.draw.rect(screen,backcard[back_cardposition],[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
            back_cardposition = back_cardposition + 1

    time.sleep(0.3)
    pygame.display.flip()
    if selection1 == True and selection2 == True:
        if color1 != color2:
            backcard[value1] = SKY_BLUE
            backcard[value2] = SKY_BLUE
        else:
            match = match + 1
        selection1 = False
        selection2 = False

    pygame.draw.rect(screen, WHITE, [5, 225, 215, 70], 3)
    if match == 8:
            screen.blit(Surf2,(35 ,250))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()



    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
