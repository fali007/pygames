import os
import random
import pygame
import math
import sys
from pygame.locals import *

class Player(object):
    def __init__(player):
        player.rect = pygame.rect.Rect((64, 54, 16, 16))

    def draw(player, surface):
        pygame.draw.rect(screen, (0, 0, 128), player.rect)
class items(object):
    def __init__(player,i,j):
        player.rect = pygame.rect.Rect((16*i+i, 16*j+j, 16, 16))

    def draw(player, surface):
        pygame.draw.rect(screen, (0, 10, 20), player.rect)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("HI")

# clock = pygame.time.Clock()
pygame.init()

speed=[2,-2]

player = Player()
item=[[items(i,j) for i in range(int(600/16)-2)]for j in range(5)]

# clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((255, 255, 255))
    player.draw(screen)
    for ita in item:
        for it in ita:   
            it.draw(screen)
    player.rect = player.rect.move(speed)
    if player.rect.left < 0 or player.rect.right > 600:
        speed[0] = -speed[0]
    if player.rect.top < 0 or player.rect.bottom > 600:
        speed[1] = -speed[1]
    pygame.display.update()
    # clock.tick(40)