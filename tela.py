import pygame


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
            
#informações de inicializacao
largura = 800
altura = 600
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Button Demo')
pygame.init()
mainClock = pygame.time.Clock()
guia_fonte =  pygame.font.SysFont("ariel",30)

#botão menu
botao1 = Button("Iniciar",100,40,(largura/1.2,altura/2)) # texto, largura , altura, posição
botao2 = Button("setting", 100,40,(largura/1.2,400))
botao3 = Button("Sair",100,40,(largura/1.2,500))
credito = Button(" Este prototico esta sendo desenvolvido por : Stephan Schrtoer e Lucas texeira",800,20,(0,580))
