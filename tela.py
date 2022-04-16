import pygame
import moviepy.editor
from pygame.locals import *
from botao import*



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
    if clicar == True and botao1.top_rect.collidepoint(pygame.mouse.get_pos()):
        print("o jogo irá iniciar")
    if clicar == True and botao2.top_rect.collidepoint(pygame.mouse.get_pos()):
        print("opçoes do jogo")
    if clicar == True and botao3.top_rect.collidepoint(pygame.mouse.get_pos()):
        print("sair do jogo")
        pygame.quit()
       
    clicar = False
            

    #desenhando na tela        
    tela.fill([30,173, 235])    
    botao1.pintar()
    botao2.pintar()
    botao3.pintar()    
    botao1 = Button("Iniciar",100,40,(150,500),Blue_black,Yellow)
    botao2 = Button("opçoes", 100,40,(350,500),Blue_black,Yellow)
    botao3 = Button("Sair",100,40,(550,500),Blue_black,Yellow)
    credito.pintar()       
    pygame.display.update()
    mainClock.tick(60)
