import pygame
from pygame.locals import *
from date_botao import *
import math


def Fundo_():
    fundo_tela = pygame.image.load('img/background_game.png').convert()
    fundo_tela_largura = fundo_tela.get_width()
    rolagem = 0
    tile = math.ceil(largura/fundo_tela_largura) +1
    
    for i in range (0, tile):
        tela.blit(fundo_tela,(i * fundo_tela_largura + rolagem, 0))
    #rolando
    rolagem += 5
    
    if abs(rolagem) > fundo_tela_largura:
        rolagem = 0
    
    
    





        
