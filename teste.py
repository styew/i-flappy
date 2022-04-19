import pygame, math

pygame.init()

clock = pygame.time.Clock()
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

roda = True

fundo_tela = pygame.image.load('img/back.png')


x = 0
while roda:
    clock.tick(60)
    
    x -= 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            roda = False
    tela.blit(fundo_tela,(x,0))
    if x == -800:
        x = 0
    print("contandor")
    pygame.display.update()
    clock.tick(60)
pygame.quit()