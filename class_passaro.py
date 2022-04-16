import pygame
from pygame.locals import *
from date_botao import *

playerImg = pygame.image.load('img/frame-1.png')
playerX = 300
playerY = 100

def Player_():
    tela.blit(playerImg, (playerX, playerY))


icone = pygame.image.load('img/bird.png')