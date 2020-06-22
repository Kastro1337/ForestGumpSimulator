import pygame
import classes
from CONST import *
pygame.init()

win = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("TestGame") # windowName


player = classes.playerClass(False)
enemy = classes.playerClass(True)
ball = classes.ballClass() # actually a square
gameObjects = [player, enemy, ball]
kuerten = [player, enemy]

run = True # game running?
while run:
    pygame.time.delay(10)# 0.1 sec

    win.fill((0,0,0))
    for obj in gameObjects:
        pygame.draw.rect(win, obj.color, obj.basic())

    ball.move()

    pygame.display.update()

    keys = pygame.key.get_pressed()
    player.move(keys)
    if not (player.x in range(0,WINDOW_W - player.width)):
        player.limit()

    if ball.collidelist(kuerten) >= 0:
       ball.changeDir()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit() # no error quit S2
