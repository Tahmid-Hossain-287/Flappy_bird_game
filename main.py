'''
The movement part cannot be inside a normal function like player. It must be inside an infinite while loop a.k.a game loop that is 
inside the blitting function.
'''
import random  # This is imported for generating obastacles at random height and distance.
import time
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import pygame
from pygame.locals import *

# The thing to do next is make a whole new class for all the codes.

fps = 120
clock = pygame.time.Clock()


class Game:
    # The variables needed to initializing screen.
    screen_size = (1700, 700) # Length of screen is 1700 units and breadth is 700 units.
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

    # def __init__(self):
    # The variables needed to initializing screen.
    #self.screen_size = (1700, 700)
    #self.screen = pygame.display.set_mode(self.screen_size)
    # The variables needed for the _background method(funciton that is attached to an object).
    #self.background = None
    #self.background_rect = None
    # Vaiables relatd to the position of players.
    #self.player_y = 60
    #self.player_x = 60
    # Varables related to the obstacle class.
    #self.pipes = None
    #self.pipes_rect = None
    #self.pipe_obstacle = None
    #self.pipe_obstacle_rect = None
    #self.obstacle_height = None
    #self.rand_num = None
    # Varables related to the text class.
    #self.text = None
    #self.font = None
    #textpos = None
    # Variables ralated to or needed for the player or bird obejct.
    #self.bird = None
    #self.bird_rect = None
    #self.player_x = None

    def initialise(self):
        # Initialise screen
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)

    def _background(self):  # Fill background
        #global background, background_rect
        self.background = pygame.Surface(self.screen.get_size())
        self.background = pygame.image.load("background.png")
        self.background = self.background.convert()
        self.background = pygame.transform.scale(self.background, self.screen_size)
        self.background_rect = self.background.get_rect()

    def obstacle(self):
        # Let the gap between upper and lower pipes be 150 units.
        self.obstacle_width = 50
        self.obstacle_start_pos = 1700

        # Bottom obstacle.  
        self.bot_obstacle_length = random.randint(0, 550)
        self.bot_obstacle = pygame.Surface((self.obstacle_width, self.bot_obstacle_length))
        self.bot_obstacle_rect = self.bot_obstacle.fill((0,0,0)) # pygame.surface.fill transforms a surface object into a rect object.
        self.bot_obstacle_rect.x = self.obstacle_start_pos
        self.bot_obstacle_rect.y = 700 - self.bot_obstacle_length

        # Top obstacle.
        self.top_obstacle_length = abs(700  -150 -self.bot_obstacle_length)
        print(f"Width is {self.obstacle_width} and height is {self.top_obstacle_length}")
        self.top_obstacle = pygame.Surface((self.obstacle_width, self.top_obstacle_length))
        self.top_obstacle_rect = self.top_obstacle.fill((0,0,0)) # pygame.Surface.get_rect(self.top_obstacle)
        self.top_obstacle_rect.x = self.obstacle_start_pos
        self.top_obstacle_rect.y = 0

        # List of both obstacles.
        self.obstacle_rect_list = [self.top_obstacle_rect, self.bot_obstacle_rect]
        self.obstacle_list = [self.top_obstacle, self.bot_obstacle]

    def obstacle_pos_update(self):
        self.top_obstacle_rect.x = self.obstacle_start_pos
        self.bot_obstacle_rect.x = self.obstacle_start_pos

    def text(self):
        # Display some text
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("Flappy Bird", 1, (10, 10, 10))
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.background.get_rect().centerx
        self.background.blit(self.text, self.textpos)

    def player(self):
        # Importing the image of the bird.
        self.bird = pygame.image.load("dove.png")
        self.bird = pygame.transform.flip(self.bird, True, False)
        self.bird = pygame.transform.scale(self.bird, (self.player_x, self.player_y))
        self.bird_rect = self.bird.get_rect()
        self.bird_rect.x = 60
        self.bird_rect.y = 60


class Blit(Game):
    def blitting(self):
        # Blit everything to the screen
        game_one.initialise()
        game_one._background()
        game_one.screen.blit(game_one.background, game_one.screen_size)
        pygame.display.flip()

        # Event loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return


            # Code about the input through key presses.
            key = pygame.key.get_pressed()
            if key[K_SPACE] and game_one.bird_rect.y < 690:
                if game_one.bird_rect.y > 0:
                    game_one.bird_rect.y -= 4 # The bird flies up when the user presses the space key.

            elif game_one.bird_rect.y < 695:
                if not key[K_SPACE]:
                    game_one.bird_rect.y += 3 # The bird continues to drop due to gravity.


            # Movement of the obstacle.
            game_one.obstacle_start_pos -= 4
            if game_one.obstacle_start_pos < -10:
                # game_one.obstacle_start_pos = 1900
                game_one.obstacle()
            game_one.obstacle_pos_update()

            # Draws and updates image.
            game_one.screen.blit(game_one.background, game_one.background_rect)
            game_one.screen.blit(game_one.bird, game_one.bird_rect)
            game_one.screen.blit(game_one.top_obstacle, game_one.top_obstacle_rect)
            game_one.screen.blit(game_one.bot_obstacle, game_one.bot_obstacle_rect)
            pygame.display.flip()
            clock.tick(fps)


            # Code the game over section here.
            if game_one.bird_rect.y >= 694 or game_one.bot_obstacle_rect.colliderect(game_one.bird_rect) or game_one.top_obstacle_rect.colliderect(game_one.bird_rect):
                game_one.over = True
                game_one.game_over = pygame.font.Font(None, 100).render("Game Over!", 1, (255, 0, 0))
                game_one.game_over_pos = game_one.game_over.get_rect()
                game_one.game_over_pos.centerx = game_one.background.get_rect().centerx
                game_one.game_over_pos.centery = game_one.background.get_rect().centery
                game_one.screen.blit(game_one.game_over, game_one.game_over_pos)
                pygame.display.flip()


            if game_one.over == True:
                print("Game Over!")
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


if __name__ == '__main__':
    main()
