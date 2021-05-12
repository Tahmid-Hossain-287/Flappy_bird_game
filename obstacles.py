import pygame
import random
from pygame.locals import *
import time

fps = 120
clock = pygame.time.Clock()
def initialise():
    # Initialise screen
    pygame.init()
    global screen, screen_size
    screen_size = (1700, 700)
    screen = pygame.display.set_mode(screen_size)


def _background(): # Fill background
    global background, background_rect
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("background.png")
    background = background.convert()
    background = pygame.transform.scale(background, screen_size)
    background_rect = background.get_rect()

thing = False
def _obstacles():
    return None


def blitting():
    while True:
        obstacle = pygame.Surface((60, 450))
        obstacle_rect = pygame.Surface.get_rect(obstacle)
        screen.blit(obstacle, obstacle_rect)
        screen.blit(background, background_rect)
        screen.blit(obstacle,(300, 40), obstacle_rect)
        pygame.display.flip()
        clock.tick(fps)

initialise()
_obstacles()
_background()
blitting()