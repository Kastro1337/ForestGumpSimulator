
try:
    import pygame
    import classes
    import random
    from os import system
    from CONST import *
except:
    print('Existem arquivos faltando não instaladas \n... Provavelmente é o pygame')
    print("ou o cara esqueceu de instalar o windows")
    input() # no meu, o cmd fecha do nada
    exit()

pygame.init()






win = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Pong ping") # windowName






player = classes.playerClass(False)
enemy = classes.playerClass(True)# TODO: if else do menu dps
ball = classes.ballClass() # actually a square
gameObjects = [player, enemy, ball]
kuerten = [player, enemy]

run = True # game running?
try:
    font = pygame.font.SysFont("arial", 30)
except:
    font = pygame.font.Font(pygame.font.get_default_font(), 30)


while run: # TODO: need a fucking clock FPS
    pygame.time.delay(10) # depends on cpu speed
    win.fill((0,0,0))

    for obj in gameObjects:
        pygame.draw.rect(win, obj.color, obj.basic())

    for pad in kuerten:

        if pad.isBot: scoreHeight = 0.6
        else: scoreHeight = 0.4
        text = font.render(str(pad.score), True, (255,255,255))
        win.blit(text, (WINDOW_W - WINDOW_W * 0.98, WINDOW_H - WINDOW_H * scoreHeight))#score @ screen



    ball.move()
    pygame.display.update()

    keys = pygame.key.get_pressed()
    player.move(keys)
    if enemy.isBot:
        enemy.x += (ball.x - (enemy.x + enemy.width / 2))* difficulty[level]  #* enemy.velocity #gotta go fast # few changes, computer not invencible

    for pad in kuerten:
        if not (pad.x in range(0,WINDOW_W - pad.width)):
            pad.limit()

    if ball.collidelist(kuerten) >= 0:
        ball.changeDir()

    if ball.x > (WINDOW_W - ball.width) or ball.x < 0 :
        ball.changeDirX()

    if ball.y <= 0:
        player.addScore()
        ball.reset()

    elif ball.y >= WINDOW_H:
        enemy.addScore()
        ball.reset()





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit() # no error quit S2
