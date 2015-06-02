import pygame
from sys import exit
from pygame.locals import *
import math


class PhysicalWorld():
	def __init__(self, ground=200,
					 length=900, width=600):
		self.worldOflength = length
		self.worldOfwidth = width
		self.worldOfground = width - ground
		self.gravity = 10
		self.time = 0
		self.objectLists = []
		self.world = self.create_new_world()
		self.hit = False
	
	def create_new_world(self):
		l = self.worldOflength
		w = self.worldOfwidth
		g = self.worldOfground
		world = pygame.display.set_mode((l, w), 0, 32)
		world.fill((255, 255, 255))
		pygame.draw.line(world, (0, 0, 0), (0, g), (l, g), 5)
		pygame.display.set_caption("For Joy")
		return world
	
	def add_object(self, object):
		self.objectLists.append(object)
	
	def object_move(self):
		time = self.time
			
		for i in range(len(self.objectLists) - 1):
			object = self.objectLists[i]
			isHit = False
			isHitWithGround = False
			for j in range(i+1, len(self.objectLists)):
				if i == j:
					continue
				isHit = object.hit(self.objectLists[j])

				if isHit is True:
					self.objectLists[j].speedY = -self.objectLists[j].speedY
					self.objectLists[j].speedX = -self.objectLists[j].speedX
					break

			if isHit is True:
				
				object.position_y -= object.speedY * 0.2
				object.position_x -= object.speedX * 0.2	
				if j != len(self.objectLists) - 1:
					object.speedX *= 0.8
					object.speedY *= 0.8
					object.speedX = -object.speedX
					object.speedY = -object.speedY
					object.hitTimes += 1
				else:
					isHitWithGround = True
					object.speedY = -object.speedY
					object.speedX *= 0.7
					object.speedY *= 0.7
					object.hitTimes = 0
					
				
				for i in range(len(self.objectLists) - 1):
					print self.objectLists[i].isBalance
				print "====="
				if math.sqrt(math.pow(object.speedX, 2) + math.pow(object.speedY, 2)) < 1:	
					if isHitWithGround is True:
						object.isBalance = True
					if object.hit(self.objectLists[len(self.objectLists) - 1]) is False:
						if object.hitTimes >= len(self.objectLists):
							object.isBalance = True
					
				
			if object.isBalance is False:
				object.speedY += 0.005 * 10
				object.position_y += object.speedY
				object.position_x += object.speedX
			object.display()

	def run(self):
		t = Block(self.world,400,0,20,20)
		
		
		self.add_object(t)
		t = Block(self.world,380,50,60,20)
		
		
		self.add_object(t)
		t = Block(self.world,400,100,20,20)
		
		
		self.add_object(t)
		t = Block(self.world,200,0,20,20)
		t.speedX = 1
		t.speedY = -1
		
		self.add_object(t)
		
		
		
		w = Block(self.world,0,400,900,200)
		self.add_object(w)
		
		
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					exit()
			#w.display()
			self.time += 1
			self.create_new_world()
			self.object_move()
			
			pygame.display.flip()


class Block():
	def __init__(self, world, x=0, y=0, length=10, width=10):
		self.m_length = length
		self.m_width = width
		self.position_x = x
		self.position_y = y
		self.centerPoint = ((2*self.position_x + self.m_length) / 2, 
									(2*self.position_y + self.m_width) / 2)
		self.m_world = world
		self.degree = 0
		self.surf = pygame.Surface((length, width))
		self.block = Rect(0, 0, length, width)
		self.speedX = 0
		self.speedY = 0
		self.isBalance = False
		self.hitTimes = 0
		
	
	def hit(self, other):
		dx = math.fabs(self.centerPoint[0] - other.centerPoint[0])
		dy = math.fabs(self.centerPoint[1] - other.centerPoint[1])
		if dx <= (self.m_length/2 + other.m_length/2):
			if dy <= (self.m_width/2 + other.m_width/2):
				return True
		return False
		
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



t = PhysicalWorld()
t.run()