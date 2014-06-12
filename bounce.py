#!/usr/bin/env python

import pygame, sys, random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
pygame.display.set_caption("Bounce!")

# Window should be rectangular and tall for line to bounce up and
# down in
window = pygame.display.set_mode((380,700))
font = pygame.font.Font('freesansbold.ttf', 25)	


# May need colours at some point
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)


#start = True
#spacebar_pressed = False

score = 0
bounce = 0

# Controls location of bar on screen
x = 640
# Use this to keep bar moving up and down
x_change = 10


# Rules for the red rectangle

rect_top = random.randint(40, 660)
rect_bottom = rect_top - 30




#Two different sounds - a ding for if you hit space bar at correct
#time, a buzz for incorrect timing
ding = pygame.mixer.Sound('ding.wav')
buzz = pygame.mixer.Sound('buzz.wav')

while True:
	window.fill(BLACK)
	pygame.draw.rect(window, WHITE, (10, x, 360, 5))
	pygame.draw.rect(window, RED, (10, rect_top, 360, 5))
	pygame.draw.rect(window, RED, (10, rect_bottom, 360, 5))


	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				if (x - 5) <= rect_top and (x + 5) >= rect_bottom:
					ding.play()
					score +=1
					rect_top = random.randint(40, 660)
					rect_bottom = rect_top - 30
					bounce = 0
				else:
					buzz.play()
					score = 0
					bounce = 0
				
	if x > 650:
		x_change *= -1
		bounce += 1

	elif x < 1:
		x_change *= -1
		bounce += 1

	if bounce > 1:
		buzz.play()
		score = 0
	
	
	x += x_change
		
	# Scores and mandatory updates
	text = font.render("Score: " + str(score), True, WHITE)
	window.blit(text, (10, 660))
	pygame.display.update()
	fpsClock.tick(30)
