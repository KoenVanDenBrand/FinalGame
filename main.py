import pygame, sys, time, random
from pygame.locals import *
size=[500,500]
pygame.init()
screen=pygame.display.set_mode(size)

# Colours
LIME = (0,255,0)
RED = (255, 0, 0)
BLACK = (0,0,0)
PINK = (255,102,178)
SALMON = (255,192,203)
WHITE = (255,255,255)
LIGHT_PINK = (255, 181, 197)
SKY_BLUE = (176, 226, 255)
screen.fill(BLACK)

# Width and Height of game box
width=50
height=50

# Margin between each cell
margin = 5

grid=[]
for row in range(12):
    grid.append([])
    for column in range(12):
        grid[row].append(0) # Append a cell


# Set title of screen
pygame.display.set_caption("Memory Game")

#Keeps game going until done
done=False

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

def cards():
    cards = []
    card1 = pygame.draw.rect(screen,red,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])
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
            grid[row][column]=1
            print(pos,"Grid coordinates: ",row,column)


    # Draw the grid
    for row in range(6):
        for column in range(6):
            color = SKY_BLUE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])

    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
