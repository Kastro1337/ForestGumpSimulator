#class file

import pygame

WINDOW_H = 640
WINDOW_W = 800

pygame.init()
class playerClass():
    def __init__(self):
        self.x = WINDOW_W / 2
        self.y = WINDOW_H - (WINDOW_H/8)
        self.width = 80
        self.height = 20
        self.velocity = 7
        self.color = (255, 0, 0)

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= self.velocity
        if keys[pygame.K_RIGHT]: self.x += self.velocity
        #if keys[pygame.K_DOWN]: self.y += self.velocity
        #if keys[pygame.K_UP]: self.y -= self.velocity
        #print(self.x) # debug purposes

    def limit(self):
        if self.x >= WINDOW_W - self.width:
            self.x = WINDOW_W - self.width
        elif self.x <= 0:
            self.x = 0
        else:
            print("fudeu") # translate to "has fucked"

    def basic(self):
        return (self.x, self.y, self.width, self.height)





class ballClass():
    def __init__(self):
        self.x = 50
        self.y = 50
        self.center = (self.x, self.y)
        self.radius = 6
        self.color = (255,255,255)
        self.velocity = 1

    def move(self):
        self.y += self.velocity
        self.center = (self.x, self.y)
        print(self.y)
        #TODO: move diagonaly
