import pygame

class Button():
    def __init__(self,text,largura,altura,posicao,color1,color2):
        #retangulo aonde ficará o texto
        self.top_rect = pygame.Rect(posicao,(largura,altura))
        self.top_color = color1
        
        #texto em si posto no retangulo
        self.text_surf = guia_fonte.render(text,True,color2)
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

#cores 
Black = "#000814"
Blue_black = "#001D3D"
Blue = "#003566"
Yellow = "#FFC300"
White_yello2 = "#FFD60A"
White = "#fffdf7"


#botão menu
botao1 = Button("Iniciar",100,40,(150,500),Blue_black,Yellow) # texto, largura , altura, posição , cor_rect, cor_text
botao2 = Button("setting", 100,40,(350,500),Blue_black,Yellow)
botao3 = Button("Sair",100,40,(550,500),Blue_black,Yellow)
credito = Button(" Este prototico esta sendo desenvolvido por : Stephan Schrtoer e Lucas texeira",800,20,(0,580),White,Blue)

#Informaçoes do cursos
clicar = False
