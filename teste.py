import pygame, math

pygame.init()

clock = pygame.time.Clock()
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

roda = True

fundo_tela = pygame.image.load('img/background_game.png').convert()
fundo_tela_largura = fundo_tela.get_width()
rolagem = 0
tile = math.ceil(largura/fundo_tela_largura) + 1


while roda:
    clock.tick(60)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            roda = False

    pygame.display.update()
pygame.quit()