import pygame
from pygame.locals import *
from date_botao import *


def Player_():
    tela.blit(playerImg, (playerX, playerY))


icone = pygame.image.load('img/bird.png')
playerImg = pygame.image.load('img/frame-1.png')
playerX = 300
playerY = 100

def plot_personagem(posicao):
    personagem = pygame.image.load('img/frame-1.png')
    tela.blit(personagem,posicao)
    
       
def game_():
    frame = pygame.time.Clock()
    tela.fill(White)
    x=300
    y=200 ; yf = y ; contador = 0
    subir = False
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                subir = True
                print("step 1")
                yf = y - 120

        if subir == True:
            y -= 12
            tela.fill(White)
            contador += 1
        if contador == 10:
            subir = False ; contador = 0
        if subir == False:
            y += 7
            print("step2")
            tela.fill(White)
        plot_personagem((x,y))
        print("y",y,"yf",yf) 
        pygame.display.update()
        frame.tick(60)
    print("Erro")
   



