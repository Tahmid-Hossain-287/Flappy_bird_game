import pygame 
from pygame.locals import *

def main():
	''' There is going to be three parts of code. The screen, background and text.'''
	# We are initializing the screen.
	pygame.init()
	screen = pygame.display.set_mode((150, 50)) # This line creates our window according to the given size.
	pygame.display.set_caption("Welcome to Flappy Birds!") # Sets the name of our window's title.

	# Code for filling up the background.
	background = pygame.Surface(screen.get_size()) # We have created pygame surface object with the size of screen that we have already created in the screen part. 
	background = background.convert() # We convert the surface into a single pixel format.This is done 
	# to increase the rendering process.
	background.fill((250, 250, 250)) # We fill the surface with white.

    # Code for text.
	font = pygame.font.Font(None, 36) # Font object is created which takes a font file(if any) and font size arguments.
	text = font.render("I am under water!", 1, (10,10,10)) # We create our text object which takes the the 
	# text that is to be printed, anti-aliasing(1 or 0) and the value of the color of text in RGB.
	text_position = text.get_rect() # We create a rectangular body covering the text object we made in the 
	# previous line.
	text_position.centerx = background.get_rect().centerx # We align the center of our text to be printed with 
	# the center of our background.

	# Now, we have to actually render our game objects.If we don't and run our code as it is now, we will see 
	# nothing.
	# The term for rendering object is called blitting. Means that we copy a pixel belonging to an object onto 
	# the required destination. 
	# In this case, we blit the text onto background and then blit the background onto the screen.
	

main()
