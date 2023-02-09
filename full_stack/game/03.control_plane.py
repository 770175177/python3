#!/usr/bin/python

import pygame
from pygame.locals import *
import time

def main():
	#create a window
	screen = pygame.display.set_mode((480,852), 0, 32)
	
	#load background
	background = pygame.image.load('./plane/background.png')

	x = 210
	y = 700

	#load hero
	hero = pygame.image.load('./plane/hero1.png')
	while True:
		#set background img
		screen.blit(background, (0,0))
	
		#set hero img
		screen.blit(hero, (x,y))
		
		#get event,such as keybord
		for event in pygame.event.get():
			if event.type == QUIT:
				print("exit")
				exit()

			#if press key
			elif event.type == KEYDOWN:
				#if press a or left
				if event.key == K_a or event.key == K_LEFT:
					x -= 5
					print('left')

				elif event.key == K_d or event.key == K_RIGHT:
					x += 5
					print('right')

				elif event.key == K_SPACE:
					print('space')

		#renew display contents
		pygame.display.update()

		time.sleep(0.01)

if __name__ == "__main__":
	main()
