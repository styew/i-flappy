import pygame
from pygame.locals import *
from botao import*

while True:
    
    #evento de interação a tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    #desenhando na tela        
    tela.fill([30,173, 235])
    botao1.pintar()
    botao2.pintar()
    botao3.pintar()
    credito.pintar()

            
    pygame.display.update()
    mainClock.tick(60)
