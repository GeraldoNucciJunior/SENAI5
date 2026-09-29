#pip instal pygame

import pygame
pygame.init()
LARGURA, ALTURA = 640,480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

PRETO = (255,10,10)

rodando = True


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        tela.fill(PRETO)
        pygame.display.flip()
        relogio.tick(60)
paygame.quit()