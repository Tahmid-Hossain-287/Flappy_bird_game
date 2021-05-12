import random  # This is imported for generating obastacles at random height and distance.
import time

import pygame
from pygame.locals import *

# The thing to do next is make a whole new class for all the codes.

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


def obstacle():
    global pipes, pipes_rect, pipe_obstacle, pipe_obstacle_rect, obstacle_height, rand_num
    pipes = pygame.image.load("black_piller.png")
    pipe_obstacle = pygame.Surface((50, 500))
    pipe_obstacle_rect = pipe_obstacle.get_rect()
    pipes_rect = pipes.get_rect()
    pipes = pygame.transform.scale(pipes, (120, 190))
    rand_num = random.randint(1, 100)
    print(rand_num)
    obstacle_height = 1700 - rand_num
    print(obstacle_height)

def text():
    # Display some text
    global text, font, textpos
    font = pygame.font.Font(None, 36)
    text = font.render("Flappy Bird", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)


player_y = 60
player_x = 60


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
        if key[K_SPACE] and player_y < 690:
            if player_y > 0:
                player_y -= 5.5 # The bird flies up when the user presses the space key.

        over = False

        if player_y < 690:
            if not key[K_SPACE]:
                player_y += 2 # The bird continues to drop due to gravity.

        else:
            # Code the game over section here.
            over = True
            game_over = pygame.font.Font(None, 100).render("Game Over!", 1, (255, 0, 0))
            game_over_pos = game_over.get_rect()
            game_over_pos.centerx = background.get_rect().centerx
            game_over_pos.centery = background.get_rect().centery
            background.blit(game_over, game_over_pos)

        # Update image.
        screen.blit(background, background_rect)
        screen.blit(pipes, (200, 600),pipes_rect)
        screen.blit(bird, (player_x, player_y), bird_rect)
        screen.blit(pipe_obstacle, (170, rand_num),pipe_obstacle_rect)
        pygame.display.flip()
        clock.tick(fps)
        if over == True:
         time.sleep(5)
         return

def main():
    initialise()
    _background()
    obstacle()
    text()
    player()
    blitting()

if __name__ == '__main__': main()
