#pip instal pygame

import pygame
pygame.init()
LARGURA, ALTURA = 640,480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

preto = (255,10,10)

azul_fundo = (20,30,60)
vermelho =(220,20,60)
verde = (00,82,00)
amarelo = (240,22,80)
branco= (255,255,255)

rodando = True


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        tela.fill(azul_fundo)
        pygame.display.flip()
        pygame.draw.rect(tela, vermelho,(50,50,200,120))
        pygame.draw.rect(tela, verde, (300,50,120,120),10)
        pygame.draw.circle(tela, amarelo, (150,320),60)
        pygame.draw.line(tela, branco, (300,300),(600,200),20)
        pygame.display.flip()


        relogio.tick(60)
pygame.quit()