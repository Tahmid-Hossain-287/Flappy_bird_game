'''
The movement part cannot be inside a normal function like player. It must be inside an infinite while loop a.k.a game loop that is 
inside the blitting function.
'''
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
    over = False

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
        self.pipe_obstacle_rect = self.pipe_obstacle.get_rect()
        self.pipes_rect = self.pipes.get_rect()
        self.pipes = pygame.transform.scale(self.pipes, (120, 190))
        self.rand_num = random.randint(1, 100)
        print(self.rand_num)
        self.obstacle_height = 1700 - self.rand_num
        print(self.obstacle_height)

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
        self.bird = pygame.image.load("dove.png")
        self.bird = pygame.transform.flip(self.bird, True, False)
        self.bird_rect = self.bird.get_rect()
        self.bird = pygame.transform.scale(self.bird, (self.player_x, self.player_y))


class Blit(Game):
    def blitting(self):
        #global game_one
        # Blit everything to the screen
        game_one.initialise()
        game_one._background()
        game_one.screen.blit(game_one.background, game_one.screen_size)
        pygame.display.flip()

        # Event loop
        while True:
            # global player_x, player_y

            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            # Code about the input through key presses.
            key = pygame.key.get_pressed()
            if key[K_SPACE] and game_one.player_y < 690:
                if game_one.player_y > 0:
                    game_one.player_y -= 5.5 # The bird flies up when the user presses the space key.

            game_one.over = False

            if game_one.player_y < 690:
                if not key[K_SPACE]:
                    game_one.player_y += 2 # The bird continues to drop due to gravity.

            else:
            # Code the game game_one.over section here.
                game_one.over = True
                game_one.over = pygame.font.Font(None, 100).render("Game game_one.over!", 1, (255, 0, 0))
                game_one.over_pos = game_one.over.get_rect()
                game_one.over_pos.centerx = game_one.background.get_rect().centerx
                game_one.over_pos.centery = game_one.background.get_rect().centery
                background.blit(game_one.over, game_one.over_pos)


            # Update image.
            game_one.screen.blit(game_one.background, game_one.background_rect)
            game_one.screen.blit(game_one.pipes, (200, 600),game_one.pipes_rect)
            game_one.screen.blit(game_one.bird, (game_one.player_x, game_one.player_y), game_one.bird_rect)
            game_one.screen.blit(game_one.pipe_obstacle, (170, game_one.rand_num),game_one.pipe_obstacle_rect)
            pygame.display.flip()
            clock.tick(fps)
            if game_one.over == True:
                time.sleep(5)
                return

game_one = Game()  # Initialised the game class.
should_blit = Blit()

def main():
    game_one.initialise()
    game_one._background()
    game_one.obstacle()
    game_one.text()
    game_one.player()
    should_blit.blitting()

if __name__ == '__main__': main()
