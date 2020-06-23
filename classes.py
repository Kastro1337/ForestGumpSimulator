#class file
import pygame
import random
from CONST import *


pygame.init()




class playerClass(pygame.Rect):
    def __init__(self, isBot):

        self.x = WINDOW_W / 2
        if isBot:
            self.y = WINDOW_H/10
        else:
            self.y = WINDOW_H - (WINDOW_H/8)
        self.width = 80
        self.height = 20
        self.velocity = playerSpeed
        self.color = (255,255,255)
        self.isBot = isBot
        self.score = 0



    def move(self,keys):
        if keys[pygame.K_LEFT]: self.x -= self.velocity
        if keys[pygame.K_RIGHT]: self.x += self.velocity

    def limit(self):
        if self.x >= WINDOW_W - self.width:
            self.x = WINDOW_W - self.width
        elif self.x <= 0:
            self.x = 0
        else:
            print("fudeu") # translate to "has fucked"

    def basic(self):
        return (self.x, self.y, self.width, self.height)

    def addScore(self):
        self.score += 1









class ballClass(pygame.Rect):
    def __init__(self):
        self.x = WINDOW_W / 2
        self.y = WINDOW_H / 2
        self.lado = 15
        self.width, self.height = self.lado, self.lado # not necessary, just use lado
        self.velocity = ballSpeed * random.choice([-1,1])
        self.angulo = ballSpeed * random.choice([-1,1])
        self.color = (255,255,255)


    def basic(self):
        return (self.x, self.y, self.width, self.height)


    def move(self):
        self.y += self.velocity
        self.x += self.angulo



    def changeDir(self):
        self.velocity = -self.velocity
        self.angulo = random.randint(-ballSpeed*2,ballSpeed*2) # just for fun

        #print("changed")

    def changeDirX(self):

        self.angulo = -self.angulo

    def reset(self):
        self.x = WINDOW_W / 2
        self.y = WINDOW_H / 2
        self.velocity = ballSpeed * random.choice([-1,1])
        self.angulo = ballSpeed * random.choice([-1,1])
        pygame.time.delay(250)
