import os
import random
import pygame
import math
import sys

class box(pygame.sprite.Sprite):
    def __init__(self, color, width, height,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.rect.center=(x,y)
class plat(pygame.sprite.Sprite):
    def __init__(self, color, width, height,x,y):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface([width, height])
       self.image.fill(color)
       self.rect = self.image.get_rect()
       self.rect.center=(x,y)
    def move_r(self,len):
        self.rect.x+=len
    def move_l(self,len):
        self.rect.x-=len

screen = pygame.display.set_mode((600, 700))
speed=[2,-2]

player=box((0,0,0),16, 16,54,64)
item=[[box((0,0,0),16, 16, 16*i+i,16*j+j) for i in range(int(600/16)-1)]for j in range(10)]
base=plat((20,0,0),100,20,300,650)

allSpritesLayered=pygame.sprite.LayeredUpdates()
allSprites = pygame.sprite.Group()

for i in item:
    for j in i:
        allSprites.add(j)
allSprites.add(player)
allSprites.add(base)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0, 0, 255))
    allSpritesLayered.empty()
    for sprite in allSprites:
        allSpritesLayered.add(sprite,layer = sprite.rect.y)
    allSpritesLayered.draw(screen)  
    player.rect = player.rect.move(speed)
    if player.rect.left < 0 or player.rect.right > 600:
        speed[0] = -speed[0]
    if player.rect.top < 0 or player.rect.bottom > 700:
        speed[1] = -speed[1]
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        base.move_l(5)
    if keys[pygame.K_RIGHT]:
        base.move_r(5)
    
    for i in allSprites:
        if i==player:
            continue
        else:
            if pygame.sprite.collide_rect(i,player):
                if player.rect.top<=i.rect.bottom or player.rect.bottom>=i.rect.top:
                    speed[0]=-speed[0]
                if player.rect.left<=i.rect.right or player.rect.right>=i.rect.left:
                    speed[1]=-speed[1]
                if i!=base:
                    allSprites.remove(i)
    pygame.display.update()