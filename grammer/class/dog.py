#!/usr/bin/python3

class Dog:
	
	def __init__(self, petname, temp):
		self.name = petname
		self.temperature = temp
	
	def status(self):
		print("dog name is ", self.name)
		print("dog temperature is ", self.temperature)
		pass

	def setTemperature(self, temp):
		self.temperature = temp
		pass

	def bark(self):
		print("woof!")
		pass
pass

sizzles = Dog("lassie", 23)
sizzles.status()
sizzles.setTemperature(40)
sizzles.status()
