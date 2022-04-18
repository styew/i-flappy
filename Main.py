import pygame
from pygame.locals import *
from date_botao import*
from class_passaro import *
from class_backgroun import *

#titulo & icone 

pygame.display.set_caption("I-Flappy")
pygame.display.set_icon(icone)
while True:
    
    #evento de interação a tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if event.type == MOUSEBUTTONDOWN:
        print(pygame.mouse.get_pos()) # checagem de comando
        clicar = True
    if botao1.top_rect.collidepoint(pygame.mouse.get_pos()):
        botao1 = Button("INICIAR",100,40,(150,500),Blue,White)  
    if botao2.top_rect.collidepoint(pygame.mouse.get_pos()):
        botao2 = Button("OPEÇOES", 100,40,(350,500),Blue_black,White) 
    if botao3.top_rect.collidepoint(pygame.mouse.get_pos()):
        botao3 = Button("SAIR",100,40,(550,500),Blue_black,White)  
    #comandos dos clicks do menu
    if clicar == True and botao1.top_rect.collidepoint(pygame.mouse.get_pos()):
        print("o jogo irá iniciar")
        running = True
    if clicar == True and botao2.top_rect.collidepoint(pygame.mouse.get_pos()):
        print("opçoes do jogo")
    if clicar == True and botao3.top_rect.collidepoint(pygame.mouse.get_pos()):
        print("sair do jogo")
        pygame.quit()
       
    clicar = False
            

    #desenhando na tela
    Fundo_()
    botao1.pintar()
    botao2.pintar()
    botao3.pintar()    
    botao1 = Button("Iniciar",100,40,(150,500),Blue_black,Yellow)
    botao2 = Button("opçoes", 100,40,(350,500),Blue_black,Yellow)
    botao3 = Button("Sair",100,40,(550,500),Blue_black,Yellow)
    credito.pintar()      
    Player_()
    pygame.display.update()
    mainClock.tick(60)
