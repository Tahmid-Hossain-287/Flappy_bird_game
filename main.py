import pygame
from pygame.locals import *


fps = 120
clock = pygame.time.Clock()


def initialise():
    # Initialise screen
    pygame.init()
    global screen, screen_size
    screen_size = (1700, 700)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Basic Pygame program')


def _background(): # Fill background
    global background, background_rect
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("background.png")
    background = background.convert()
    background = pygame.transform.scale(background, screen_size)
    background_rect = background.get_rect()

def text():
    # Display some text
    global text, font, textpos
    font = pygame.font.Font(None, 36)
    text = font.render("Flappy Bird", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

player_x = 60
player_y = 60



def player():

    # Importing the image of the bird.
    global bird, bird_rect
    global player_x
    bird = pygame.image.load("dove.png")
    bird = pygame.transform.flip(bird, True, False)
    bird_rect = bird.get_rect()
    bird = pygame.transform.scale(bird, (player_x, player_y))


def blitting():

    # Blit everything to the screen
    screen.blit(background, screen_size)
    pygame.display.flip()

    # Event loop
    while True:
        global player_x, player_y
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # Code about the input through key presses.
        key = pygame.key.get_pressed()
        if key[K_SPACE]:
            player_y -= 4 # The bird flies up when the user presses the space key.

        if player_y < 690:
            if not key[K_SPACE]:
                player_y += 1 # The bird continues to drop due to gravity.
        else:

            return # Code the game over section here.


        # Update image.
        screen.blit(background, background_rect)
        screen.blit(bird,(player_x, player_y), bird_rect)
        pygame.display.flip()
        clock.tick(fps)


def main():
    initialise()
    _background()
    text()
    player()
    # player_movement()
    blitting()

if __name__ == '__main__': main()
