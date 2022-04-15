import pygame

class Menu():
    def __init__(self,text,largura,altura,posicao):
        #top retangulo
        self.top_rect = pygame.Rect(posicao,(largura,altura))
        self.top_color = "#475F77"
        
        #texto
        self.text_surf = guia_fonte.render(text,True,"#ffffff")
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def pintar(self):
        pygame.draw.rect(tela,self.top_color,self.top_rect)
        tela.blit(self.text_surf,self.text_rect)

#resolução
largura = 600
altura = 800

#tela
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Button Demo')

#informações para rodar
rodar = True
pygame.init()
guia_fonte =  pygame.font.SysFont("ariel",30)
botao1 = Menu("teste",200,40,(300,200))

while rodar:
    

    
    #evento de interação a tela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodar = False 
            
    tela.fill([30,173, 235])
    botao1.pintar()
    pygame.display.update()
    
pygame.quit()