import pygame
from pygame.locals import *

class Button():
    def __init__(self,text,largura,altura,posicao):
        #retangulo aonde ficará o texto
        self.top_rect = pygame.Rect(posicao,(largura,altura))
        self.top_color = "#475F77"
        
        #texto em si posto no retangulo
        self.text_surf = guia_fonte.render(text,True,"#ffffff")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def pintar(self):
        pygame.draw.rect(tela,self.top_color,self.top_rect)
        tela.blit(self.text_surf,self.text_rect)

#resolução
largura = 800
altura = 600

#tela
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Button Demo')
fps = pygame.time.Clock()

#informações para rodar
rodar = True
pygame.init()
guia_fonte =  pygame.font.SysFont("ariel",30)


#criação de texto:
botao1 = Button("Iniciar",100,40,(largura/1.2,altura/2)) # texto, largura , altura, posição
botao2 = Button("setting", 100,40,(largura/1.2,200))
botao3 = Button("Sair",100,40,(largura/1.2,100))
credito = Button(" Este prototico esta sendo desenvolvido por : Stephan Schrtoer e Lucas texeira",800,20,(0,580))
#cursor
clicar = False

while rodar:
    fps.tick(60)
    #evento do cursor
    if clicar:
        print(pygame.mouse.get_pos())
    #evento de interação a tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False 
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicar =  True
        if event.type == MOUSEBUTTONUP:
            clicar = False
    
    #desenhando na tela        
    tela.fill([30,173, 235])
    botao1.pintar()
    botao2.pintar()
    botao3.pintar()
    credito.pintar()
    #atualizacao
    pygame.display.update()

pygame.quit()