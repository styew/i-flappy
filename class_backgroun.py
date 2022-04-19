from genericpath import exists
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

def plot_personagem(posicao):
    personagem = pygame.image.load('img/frame-1.png')
    tela.blit(personagem,posicao)
    
       
def game_():
    frame = pygame.time.Clock()
    tela.fill(White)
    x=300
    y=200 ; yf = y ; contador = 0
    subir = False ; xx=0
    while running:
        fundo_game(xx)
        print("valor saida",xx)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYUP:
                subir = True
                print("step 1")
                yf = y - 120

        if subir == True:
            y -= 12
            fundo_game(xx)
            contador += 1
        if contador == 10:
            subir = False ; contador = 0
        if subir == False:
            y += 7
            print("step2")
            fundo_game(xx)
        plot_personagem((x,y))
        xx -= 10
        if xx == -800:
            xx = 0
        #print("y",y,"yf",yf) 
        pygame.display.update()
        frame.tick(60)
    print("Erro")

   
def fundo_game(x):
    tela = pygame.display.set_mode((largura, altura))
    fundo_tela = pygame.image.load('img/back.png') 
    tela.blit(fundo_tela,(x,0))
        




game_()
        
