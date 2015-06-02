import pygame
from sys import exit
from pygame.locals import *


class PhysicalWorld():
	def __init__(self, ground=200,
					 length=900, width=600):
		self.worldOflength = length
		self.worldOfwidth = width
		self.worldofground = width - ground
		self.gravity = 10
		self.time = 0
		self.objectLists = []
		self.world = self.create_new_world()
		self.hit = False
	
	def create_new_world(self):
		l = self.worldOflength
		w = self.worldOfwidth
		g = self.worldofground
		world = pygame.display.set_mode((l, w), 0, 32)
		world.fill((255, 255, 255))
		pygame.draw.line(world, (0, 0, 0), (0, g), (l, g), 5)
		return world
	
	def add_object(self, object):
		self.objectLists.append(object)
	
	def object_move(self):
		time = self.time
		
		
		for object in self.objectLists:
			print object.position_y + object.m_length
			print object.speed
			if object.position_y + object.m_length >= self.worldofground:
				self.hit = True
				object.speed = object.speed * 0.85
				object.position_y = self.worldofground - object.m_length
				#self.time = 0
			
			if self.hit is False:
				object.speed += 0.0005 * 10
				object.position_y += object.speed
				
			else:
				object.speed -= 0.0005 * 10
				object.position_y -= object.speed
				if object.speed <= 0:
					object.speed = 0
					self.hit = False
			object.degree += 1
			object.display()
	
	def run(self):
		t = Block(self.world,200,10,50,50)
		self.add_object(t)
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					exit()
			
			self.time += 1
			self.create_new_world()
			self.object_move()
			pygame.display.flip()
			


class Block():
	def __init__(self, world, x=0, y=0, length=10, width=10):
		self.m_length = length
		self.m_width = width
		self.centerPoint = (x / 2, y / 2)
		self.position_x = x
		self.position_y = y
		self.m_world = world
		self.degree = 0
		self.surf = pygame.Surface((length, width))
		self.block = Rect(0, 0, length, width)
		self.speed = 0
	
	def hit(hit):
		pass 
	def display(self):
		self.surf.fill((255, 255, 255))
		self.surf.set_colorkey((255, 255, 255))
		pygame.draw.rect(self.surf, (0, 0, 0), self.block)
		rorateSurf = pygame.transform.rotate(self.surf, self.degree)
		rect = rorateSurf.get_rect()
		self.centerPoint = ((2*self.position_x + self.m_length) / 2, 
									(2*self.position_y + self.m_width) / 2)
		rect.center = self.centerPoint
		self.m_world.blit(rorateSurf, rect)
		
		
		
		
		
		
'''
screen = pygame.display.set_mode((900, 600), 0, 32)
screen.fill((255, 255, 255))
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	pygame.display.flip()
'''

t = PhysicalWorld()
t.run()