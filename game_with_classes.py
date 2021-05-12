import random  # This is imported for generating obastacles at random height and distance.
import time

import pygame
from pygame.locals import *

# The thing to do next is make a whole new class for all the codes.

fps = 120
clock = pygame.time.Clock()

class Game:
    #The variables needed to initializing screen.
    screen_size = (1700, 700)
    screen = pygame.display.set_mode(screen_size)
    # The variables needed for the _background method(funciton that is attached to an object).
    background = None
    background_rect = None
    # Vaiables relatd to the position of players.
    player_y = 60
    player_x = 60
    # Varables related to the obstacle class.
    pipes = None
    pipes_rect = None
    pipe_obstacle = None
    pipe_obstacle_rect = None
    obstacle_height = None
    rand_num = None
    # Varables related to the text class.
    text = None
    font = None
    textpos = None
    # Variables ralated to or needed for the player or bird obejct.
    bird = None
    bird_rect = None
    player_x = None

    #def __init__(self):
        ## The variables needed to initializing screen.
        #self.screen_size = (1700, 700)
        #self.screen = pygame.display.set_mode(self.screen_size)
        ## The variables needed for the _background method(funciton that is attached to an object).
        #self.background = None
        #self.background_rect = None
        ## Vaiables relatd to the position of players.
        #self.player_y = 60
        #self.player_x = 60
        ## Varables related to the obstacle class.
        #self.pipes = None
        #self.pipes_rect = None
        #self.pipe_obstacle = None
        #self.pipe_obstacle_rect = None
        #self.obstacle_height = None
        #self.rand_num = None
        ## Varables related to the text class.
        #self.text = None
        #self.font = None
        #textpos = None
        ## Variables ralated to or needed for the player or bird obejct.
        #self.bird = None
        #self.bird_rect = None
        #self.player_x = None

    def initialise(self):
        # Initialise screen
        pygame.init()
        #global screen, screen_size
        self.screen_size = (1700, 700)
        self.screen = pygame.display.set_mode(self.screen_size)

    def _background(self): # Fill background
        #global background, background_rect
        self.background = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load("background.png")
        self.background = self.background.convert()
        self.background = pygame.transform.scale(self.background, self.screen_size)
        self.background_rect = self.background.get_rect()

    def obstacle(self):
        #global pipes, pipes_rect, pipe_obstacle, pipe_obstacle_rect, obstacle_height, rand_num
        self.pipes = pygame.image.load("black_piller.png")
        self.pipe_obstacle = pygame.Surface((50, 500))
        self.pipe_obstacle_rect = pipe_obstacle.get_rect()
        self.pipes_rect = pipes.get_rect()
        self.pipes = pygame.transform.scale(pipes, (120, 190))
        self.rand_num = random.randint(1, 100)
        print(rand_num)
        self.obstacle_height = 1700 - rand_num
        print(obstacle_height)

    def text(self):
        # Display some text
        #global text, font, textpos
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Flappy Bird", 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.background.get_rect().centerx
        self.background.blit(self.text, self.textpos)


    def player(self):

        # Importing the image of the bird.
        #global bird, bird_rect, player_x
        self.bird = pygame.image.load("dove.png")
        self.bird = pygame.transform.flip(self.bird, True, False)
        self.bird_rect = self.bird.get_rect()
        self.bird = pygame.transform.scale(self.bird, (self.player_x, self.player_y))


game_one = Game()  # Initialised the game class.


def blitting():
    #global game_one
    # Blit everything to the screen
    game_one.initialise()
    game_one._background()
    game_one.screen.blit(game_one.background, game_one.screen_size)
    pygame.display.flip()

    ## Event loop
    #while True:
    #    global player_x, player_y
    #    for event in pygame.event.get():
    #        if event.type == QUIT:
    #            return

    #    # Code about the input through key presses.
    #    key = pygame.key.get_pressed()
    #    if key[K_SPACE] and player_y < 690:
    #        if player_y > 0:
    #            player_y -= 5.5 # The bird flies up when the user presses the space key.

    #    over = False

    #    if player_y < 690:
    #        if not key[K_SPACE]:
    #            player_y += 2 # The bird continues to drop due to gravity.

    #    else:
    #        # Code the game over section here.
    #        over = True
    #        game_over = pygame.font.Font(None, 100).render("Game Over!", 1, (255, 0, 0))
    #        game_over_pos = game_over.get_rect()
    #        game_over_pos.centerx = background.get_rect().centerx
    #        game_over_pos.centery = background.get_rect().centery
    #        background.blit(game_over, game_over_pos)

    #    # Update image.
    #    screen.blit(background, background_rect)
    #    screen.blit(pipes, (200, 600),pipes_rect)
    #    screen.blit(bird, (player_x, player_y), bird_rect)
    #    screen.blit(pipe_obstacle, (170, rand_num),pipe_obstacle_rect)
    #    pygame.display.flip()
    #    clock.tick(fps)
    #    if over == True:
    #     time.sleep(5)
    #     return

def main():
    #initialise()
    #_background()
    #obstacle()
    #text()
    #player()
    blitting()

if __name__ == '__main__': main()