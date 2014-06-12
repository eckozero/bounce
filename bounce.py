#!/usr/bin/env python

import pygame, sys, random, webbrowser
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
pygame.display.set_caption("Bounce!")

mousex, mousey = 0, 0

# Window should be rectangular and tall for line to bounce up and
# down in
window = pygame.display.set_mode((380,700))
font = pygame.font.Font('freesansbold.ttf', 25)	


# May need colours at some point
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)


score = 0
bounce = 0

# Controls location of bar on screen
x = 640
# Use this to keep bar moving up and down
# Amend this variable to change speed
x_change = 10


# Rules for the red rectangle
# Generate random point, then add two red lines for marker
# These variables are actually named upside down but that's not
# important
rect_top = random.randint(40, 660)
rect_bottom = rect_top - 30


#Two different sounds - a ding for if you hit space bar at correct
#time, a buzz for incorrect timing
ding = pygame.mixer.Sound('ding.wav')
buzz = pygame.mixer.Sound('buzz.wav')

playing = True
def playGame(playing, score):
	global bounce, x, x_change, rect_top, rect_bottom
	while playing:
		window.fill(BLACK)
		pygame.draw.rect(window, WHITE, (10, x, 360, 5))
		pygame.draw.rect(window, RED, (10, rect_top, 360, 5))
		pygame.draw.rect(window, RED, (10, rect_bottom, 360, 5))


	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
			if event.type == KEYDOWN:
				# Pressed space bar
				if event.key == K_SPACE:
					# Is the white line between the red ones?
					if (x - 5) <= rect_top and (x + 5) >= rect_bottom:
					# Yes. Play the sound, add one to the score
						ding.play()
						score +=1
					# Red lines need to be reinitialised
						rect_top = random.randint(40, 660)
						rect_bottom = rect_top - 30
					else:
					# No. white line not between red ones
					# Play the buzz and go to gameover
						buzz.play()
						playing = False
						
					# Reagrdless of yes or no, bounce counter must be
					# reset here
					bounce = 0
			# As above, but with mouse click instead of spacebar press
			elif event.type == MOUSEBUTTONDOWN:
				if event.button in (1,2,3):
					if (x - 5) <= rect_top and (x + 5) >= rect_bottom:
						ding.play()
						score +=1
						rect_top = random.randint(40, 660)
						rect_bottom = rect_top - 30
					else:
						buzz.play()
						playing = False
					bounce = 0
			
		if x > 650 or x < 1:
			x_change *= -1
			bounce += 1

		if bounce > 1 and score > 0:
			buzz.play()
			bounce = 0
			playing = False
	
	
		x += x_change

	# Scores and mandatory updates
		text = font.render("Score: " + str(score), True, WHITE)
		window.blit(text, (10, 660))
		pygame.display.update()
		fpsClock.tick(30)
	gameOver(playing, score)
	
def gameOver(playing, score):
	window.fill(WHITE)
	gOFont = pygame.font.Font('freesansbold.ttf', 50)
	gameOverText = gOFont.render("Game Over!", True, BLACK)
	displayScore = gOFont.render("You scored " + str(score), True, BLACK)
	queryText = font.render("Play again? Y/N", True, RED)
	
	tweetButton = font.render("Tweet your score (press T)", True, RED)
	window.blit(tweetButton, (30, 450))
	
	
	window.blit(gameOverText, (30, 200))
	window.blit(displayScore, (20, 250))
	window.blit(queryText, (30, 400))
	
	pygame.display.update()
	fpsClock.tick(30)
	while playing == False:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_y:
					score = 0
					playing = True
					playGame(playing, score)
				elif event.key == K_n:
					pygame.quit()
					sys.exit()
				elif event.key == K_t:
					message = "I%20scored%20" + str(score) + "%20on%20@KentGeek's%20game,%20Bounce.%20Can%20you%20beat%20me?%20https://github.com/eckozero/bounce"
					webbrowser.open("https://twitter.com/intent/tweet?button_hashtag=Bounce&text="+message, new=1, autoraise=True)

					
playGame(playing, score)

