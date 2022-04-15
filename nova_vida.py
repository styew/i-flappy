import pygame
from pygame.locals import *
class Main():
    #resolução
    largura = 800
    altura = 600

    #tela e icone
    tela = pygame.display.set_mode([largura, altura])
    icone = pygame.image.load('img/bird.png')
    pygame.display.set_caption('i-Flappy')
    pygame.display.set_icon(icone)    
    

    # Bird
playerImg = pygame.image.load('img/frame-1.png')
playerX = 300
playerY = 100


# coloca logo na tela
def menu_bird():
    Main.tela.blit(playerImg, (playerX, playerY))

#informações para rodar
rodar = True
pygame.init()
guia_fonte =  pygame.font.SysFont("ariel",30)


#evento de interação a tela
while rodar:
    Main.tela.fill([0, 8, 20])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False 
    
    menu_bird()
    pygame.display.update()
    
    
pygame.quit()