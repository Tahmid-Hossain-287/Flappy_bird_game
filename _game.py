# import sys, pygame
# pygame.init()

# size = width, height = 320, 240
# speed = [2, 2]
# black = 0, 0, 0

# screen = pygame.display.set_mode(size)

# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]

#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()

try:
	import sys, pygame # Imports all the necessary modules for our project.
except Exception as error:
	print("Could not import the necessary modules.The error here is ",error)

pygame.init() # This code will initialize all our modules, which means they are now ready to run.
if pygame.get_init() == True:
	print("Pygame initialized successfully.")
else:
	print("Could not initialze pygame successfully.") # This if, else block is just gonna ensure that pygame has been initialized successfully through the code pygame.init().

''' As we have already called pygame.init(), we won't have to call any other lower level init codes like
pygame.display.init(). '''

# Now, wer are going to make some global variables and store some informations in them.
fps = 32
scr_width = 289
scr_height = 511
display_screen_window = pygame.display.set_mode((scr_width, scr_height))
play_ground = scr_height * 0.8 
game_image = {}
game_audio_sound = {}
player_image = "./bird.png"
background_image = "./backgroundj.png" 
pipe_image = "./pipe.png"
_mode([screen_width, screen_height])	
