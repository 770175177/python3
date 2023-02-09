#!/usr/bin/python

import pygame
import time

def main():
	#create a window
	screen = pygame.display.set_mode((480,852), 0, 32)
	
	#load background
	background = pygame.image.load('./plane/background.png')

	#load hero
	hero = pygame.image.load('./plane/hero1.png')
	while True:
		#set background img
		screen.blit(background, (0,0))
	
		#set hero img
		screen.blit(hero, (210,700))
		
		#renew display contents
		pygame.display.update()

		time.sleep(0.01)

if __name__ == "__main__":
	main()
