import pygame
from pygame.locals import *


def initialise():
    # Initialise screen
    pygame.init()
    global screen, screen_size
    screen_size = (1700, 700)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Basic Pygame program')

def _background():
    # Fill background
    global background, background_rect
    background = pygame.Surface(screen.get_size())
    print(background)
    background = pygame.image.load("background.png")
    background = background.convert()
    background = pygame.transform.scale(background, screen_size)
    print(pygame.Surface.get_size(background))
    background_rect = background.get_rect()
    # background.fill((250, 250, 250))

def text():
    # Display some text
    global text, font, textpos 
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

def bird():
    # Importing the image of the bird.
    global bird, bird_rect
    bird = pygame.image.load("dove.png")
    bird = pygame.transform.flip(bird, True, False)
    bird_rect = bird.get_rect()
    bird = pygame.transform.scale(bird, (60, 60))


def blitting():
    # Blit everything to the screen
    screen.blit(background, screen_size)
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # Update image.
        screen.blit(background, background_rect)
        screen.blit(bird, bird_rect)
        pygame.display.flip()

def main():
    initialise()
    _background()
    text()
    bird()
    blitting()

if __name__ == '__main__': main()
