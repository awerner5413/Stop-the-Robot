# TODO:
    # you win and you lose messages
    # find dictionary api for wordbank # use google fonts - it's an API?
    # get better font and see if I can round button edges    
    # fix robot images by starting with a completed robot with the size I want, then remove each part and save    
    # Make letters "pressable" using keyboard
    # add a starting screen that says "Enter the destruct sequence before the robot destroys the world!"    
    # learn how pygame works with base Python under the hood
# FEATURES
    # add a timer
    # have the timer go faster or slower based on successful/incorrect guesses
    # have more difficult levels with shorter timers

import pygame
import os
from random import choice

pygame.init()

# Define game window
WIDTH, HEIGHT = 1500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stop the Robot!")

# Define colors
BG_COLOR = (255, 255, 255)
GRAY = (100, 100, 100)
ANNA_COLOR = (204, 255, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define images
COMPUTER_IMAGE = pygame.image.load(os.path.join('robot_pieces', 'computer_screen.jpg'))
COMPUTER = pygame.transform.scale(COMPUTER_IMAGE, (600, 450))
RH_IMAGE = pygame.image.load(os.path.join('robot_pieces', 'robot_head.png'))
RH = pygame.transform.scale(RH_IMAGE, (300, 450))
RLA_IMAGE = pygame.image.load(os.path.join('robot_pieces', 'robot_left_arm.png'))
RLA = pygame.transform.scale(RLA_IMAGE, (300, 450))
RRA_IMAGE = pygame.image.load(os.path.join('robot_pieces', 'robot_right_arm.png'))
RRA = pygame.transform.scale(RRA_IMAGE, (300, 450))
RB_IMAGE = pygame.image.load(os.path.join('robot_pieces', 'robot_body.png'))
RB = pygame.transform.scale(RB_IMAGE, (300, 450))
RL_IMAGE = pygame.image.load(os.path.join('robot_pieces', 'robot_legs.png'))
RL = pygame.transform.scale(RL_IMAGE, (300, 450))

# Define clock
FPS = 60
clock = pygame.time.Clock()

# Define word generator
words = ['SANDWICH', 'BURRITO', 'NACHOS', 'GYROS', 'WAFFLES']


# Create button class for player input
class keyButton():
    def __init__(self, color, x, y, width, height, text='1'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, WIN):
        # Call method to draw button on the screen
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '1':
            font = pygame.font.SysFont('Arial', int((self.width + self.height)/2.5))
            text = font.render(self.text, 1, BLACK)
            WIN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver (self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True

    def disappear (self, text):
        self.color = WHITE
        self.text = text


# Create class to display the code blank initially and visible as it is guessed
class codeScreen():
    def __init__(self, color, x, y, width, height, text='1'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def drawInitial(self, WIN):
        # Call method to draw button on the screen
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '1':
            font = pygame.font.SysFont('Arial', int((self.width + self.height)/2.5))
            text = font.render(self.text, 1, BLACK)
            WIN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
    def drawCorrect(self):
        self.color = WHITE


def draw_stuff(WIN, COMPUTER, RH, RLA, RRA, RB, RL, counter, buttonList, codeButtons):
    WIN.fill(BG_COLOR)
    WIN.blit(COMPUTER, (850, 100))

    # Draw buttons buttons
    for i in buttonList:
        i.draw(WIN)    

    for j in codeButtons:
        j.drawInitial(WIN)

    # Draw the robots
    if counter == 1:
        WIN.blit(RL, (175, 25))
    elif counter == 2:
        WIN.blit(RB, (175, 25))
    elif counter == 3:
        WIN.blit(RRA, (175, 25))
    elif counter == 4:
        WIN.blit(RLA, (175, 25))
    elif counter == 5:
        WIN.blit(RH, (175, 25))

    pygame.display.update()


def main():
    counter = 0
    code = choice(words)

    # Create boxes to display the code for correct guesses
    LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT = 30, 50
    codeX, codeY = 925, 275
    codeButtons = []
    for i in code:
        codeButton = codeScreen(BLACK, codeX, codeY, LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT, i)
        codeButtons.append(codeButton)
        codeX = codeX + 42
    
    # Create the buttons to submit input
    alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    buttonList = []
    x = 50
    for i in alphaList:    
        letter = i
        buttonName = f"{letter}_button"
        if x <= 1155:
            buttonName = keyButton(ANNA_COLOR, x, 700, 80, 70, letter)
        else:
            buttonName = keyButton(ANNA_COLOR, x-1105, 775, 80, 70, letter)
        buttonList.append(buttonName)
        x = x + 85
    
    # Start the game and draw the display
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            # Select a letter and then hide the button and display either a robot piece or the letter on the screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in buttonList:
                    if i.isOver(pygame.mouse.get_pos()) == True:   
                        if i.text in code:
                            for j in codeButtons:
                                if i.text == j.text:
                                    j.drawCorrect()
                        else:
                            counter += 1
                        i.disappear('1')

        draw_stuff(WIN, COMPUTER, RH, RLA, RRA, RB, RL, counter, buttonList, codeButtons)

        if counter > 5:
            main()


if __name__ == "__main__":
    main()