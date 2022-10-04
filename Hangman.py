# TODO:
# get letters to appear on lines based on letter button clicked (show all upper, only show correct inputs)
## see note in draw fxn, need event to deliver bool

# load buttons across the bottom (two rows, alpha order)
# get better font and see if I can round button edges
# you win and you lose messages
# fix robot images by starting with a completed robot with the size I want, then remove each part and save
# find dictionary api for wordbank
# use google fonts - it's an API?
# learn how pygame works with base Python under the hood

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
words = ['sandwich', 'burrito', 'nachos', 'gyros', 'waffles']


# Create button class and test button A
class button():
    def __init__(self, color, x, y, width, height, text='1'):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, WIN, letter='1'):
        # Call method to draw botton on the screen
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

        if self.text != '1':
            font = pygame.font.SysFont('Arial', 60)
            text = font.render(self.text, 1, BLACK)
            WIN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver (self, position):
        if position[0] > self.x and position[0] < self.x + self.width:
            if position[1] > self.y and position[1] < self.y + self.height:
                return True

    def disappear (self, text):
        self.color = WHITE
        self.text = text


A_button = button(ANNA_COLOR, 50, 700, 80, 70, 'A')


def draw_stuff(WIN, COMPUTER, RH, RLA, RRA, RB, RL, counter, code):
    WIN.fill(BG_COLOR)
    WIN.blit(COMPUTER, (850, 100))

    # Draw letter buttons
    A_button.draw(WIN)

    # Define and draw letter lines
    LETTER_LINE_WIDTH, LETTER_LINE_HEIGHT = 30, 5
    LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT = 30, 50
    x, y = 925, 275
    for i in code:
        LETTER_LINE = pygame.Rect(x, y, LETTER_LINE_WIDTH, LETTER_LINE_HEIGHT)
        LETTER_BOX = pygame.Rect(x, y - LETTER_BOX_HEIGHT, LETTER_BOX_WIDTH, LETTER_BOX_HEIGHT)
        pygame.draw.rect(WIN, RED, LETTER_LINE)
        pygame.draw.rect(WIN, BLACK, LETTER_BOX)
        x = x + LETTER_LINE_WIDTH + 12
    # I CAN HAVE AN EVENT RETURN BOOL FOR LETTER IN CODE AND IF TRUE THEN RENDER TEXT = i on LETTER_BOX


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

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL:
                    counter += 1

            # IS THERE A WAY TO DO THIS WITHOUT LISTING EACH BUTTON SEPARATELY???
            if event.type == pygame.MOUSEBUTTONDOWN:
                if A_button.isOver(pygame.mouse.get_pos()) == True:
                    print("A button pressed")
                    A_button.disappear('1')

        draw_stuff(WIN, COMPUTER, RH, RLA, RRA, RB, RL, counter, code)

        if counter > 5:
            main()


if __name__ == "__main__":
    main()

# FEATURES
# add a starting screen that says "Enter the destruct sequence before the robot destroys the world!"
# add a timer
# have the timer go faster or slower based on successful/incorrect guesses
# have more difficult levels with shorter timers
