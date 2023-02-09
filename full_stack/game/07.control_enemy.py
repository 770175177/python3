#!/usr/bin/python

import pygame
from pygame.locals import *
import time

class HeroPlane(object):
	def __init__(self, screen_temp):
		self.x = 210
		self.y = 700
		self.screen = screen_temp
		self.image = pygame.image.load('./plane/hero1.png')
		self.bullet_list = []

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()

	def move_left(self):
		self.x -= 5	

	def move_right(self):
		self.x += 5

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(object):
	def __init__(self, screen_temp):
		self.x = 0
		self.y = 0
		self.screen = screen_temp
		self.image = pygame.image.load('./plane/enemy0.png')
		self.direction = 'right'
		self.bullet_list = []

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()

	def move(self):
		if self.direction == 'right':
			self.x += 5
		elif self.direction == 'left':
			self.x -= 5
		
		if self.x > 430:
			self.direction = 'left'
		elif self.x < 0:
			self.direction = 'right'

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Bullet(object):
	def __init__(self, screen_temp, x, y):
		self.x = x + 40
		self.y = y - 20
		self.screen = screen_temp
		self.image = pygame.image.load('./plane/bullet.png')
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
	def move(self):
		self.y -= 5

def key_control(hero_temp):
	#get event,such as keybord
	for event in pygame.event.get():
		if event.type == QUIT:
			print("exit")
			exit()
		#if press key
		elif event.type == KEYDOWN:
			#if press a or left
			if event.key == K_a or event.key == K_LEFT:
				hero_temp.move_left()
				print('left')

			elif event.key == K_d or event.key == K_RIGHT:
				hero_temp.move_right()
				print('right')

			elif event.key == K_SPACE:
				hero_temp.fire()
				print('space')


def main():
	#create a window
	screen = pygame.display.set_mode((480,852), 0, 32)
	
	#load background
	background = pygame.image.load('./plane/background.png')

	#load hero
	hero = HeroPlane(screen)

	#load enemy
	enemy = EnemyPlane(screen)

	while True:
		#set background img
		screen.blit(background, (0,0))
	
		#set hero img
		hero.display()
		
		#set enemy img
		enemy.display()
		enemy.move()

		#renew display contents
		pygame.display.update()
	
		key_control(hero)
		
		time.sleep(0.01)

if __name__ == "__main__":
	main()
