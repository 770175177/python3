#!/usr/bin/python

import pygame
from pygame.locals import *
import time
import random

class BasePlane(object):
	def __init__(self, screen_temp, x, y, img_name):
		self.x = x
		self.y = y
		self.screen = screen_temp
		self.image = pygame.image.load(img_name)
		self.bullet_list = []

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		for bullet in self.bullet_list:
			bullet.display()
			bullet.move()
			if bullet.judge():
				self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
	def __init__(self, screen_temp):
		BasePlane.__init__(self, screen_temp, 210, 500, './plane/hero1.png') #super()__init__()


	def move_left(self):
		self.x -= 10	

	def move_right(self):
		self.x += 10

	def fire(self):
		self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(BasePlane):
	def __init__(self, screen_temp):
		BasePlane.__init__(self, screen_temp, 0, 0, './plane/enemy0.png') #super()__init__()
		self.direction = 'right'

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
		rand_num = random.randint(1, 100) 
		if rand_num == 34 or rand_num == 85:
			self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))
			#time.sleep(0.5)

class BaseBullet(object):
	def __init__(self, screen_temp, x, y, img_name):
		self.x = x# + 40
		self.y = y# - 20
		self.screen = screen_temp
		self.image = pygame.image.load(img_name)
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
	def __init__(self, screen_temp, x, y):
		BaseBullet.__init__(self,screen_temp, x+40, y-20,'./plane/bullet.png')
	def move(self):
		self.y -= 5
	def judge(self):
		if self.y < 0:
			return True
		else:
			return False

class EnemyBullet(BaseBullet):
	def __init__(self, screen_temp, x, y):
		BaseBullet.__init__(self,screen_temp, x+25, y+40,'./plane/bullet1.png')
	def move(self):
		self.y += 5
	def judge(self):
		if self.y > 852:
			return True
		else:
			return False

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
	screen = pygame.display.set_mode((480,652), 0, 32)
	
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
		enemy.fire()

		#renew display contents
		pygame.display.update()
	
		key_control(hero)
		
		time.sleep(0.01)

if __name__ == "__main__":
	main()
