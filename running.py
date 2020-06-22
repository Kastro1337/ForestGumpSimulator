import pygame
import classes

pygame.init()


WINDOW_H = 640
WINDOW_W = 800
win = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("TestGame") # windowName

player =  classes.playerClass()
ball = classes.ballClass()


run = True # game running?
while run:
    pygame.time.delay(10)# 0.1 sec

    win.fill((0,0,0))
    pygame.draw.rect(win, player.color, player.basic())
    pygame.draw.circle(win,ball.color,ball.center,ball.radius)
    ball.move()
    pygame.display.update()

    keys = pygame.key.get_pressed()
    player.move(keys)
    if not (player.x in range(0,WINDOW_W - player.width)):
        player.limit()

        '''TODO: ADD COLISSION '''




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit() # no error quit S2
