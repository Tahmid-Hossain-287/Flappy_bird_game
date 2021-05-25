import pygame 
import random
pygame.init()
import time

clock = pygame.time.Clock()

screen_size = (1700, 700)
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface( screen.get_size())
background = pygame.image.load("background.png")
background =  background.convert()
background = pygame.transform.scale( background,  screen_size)
background_rect =  background.get_rect()

bird = pygame.image.load("dove.png")
bird = pygame.transform.flip(bird, True, False)
bird_rect = bird.get_rect()
bird = pygame.transform.scale(bird, (60, 60))

pipe_obstacle = pygame.Surface((50, 500))
pipe_obstacle_rect = pipe_obstacle.get_rect()
horizontal_pos = 1400

while True:
    screen.blit(background, background_rect)
    screen.blit(bird, (200, 300), bird_rect)
    screen.blit(pipe_obstacle, (horizontal_pos, 120),pipe_obstacle_rect)
    horizontal_pos -= 5
    if horizontal_pos < 0:
        horizontal_pos = 1400
    if bird_rect.colliderect(pipe_obstacle_rect):
        print("They have collided.")
    pygame.display.flip() 
    clock.tick(120)
