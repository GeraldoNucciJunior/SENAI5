import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

fundo = (20, 30, 60)
bola = (240, 220, 80)

x = 50
y = 140
raio = 30

velocidade_x = 5
velocidade_y = 5

largura = 800
altura = 600

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    x += velocidade_x
    y += velocidade_y

    if x + raio >= largura or x - raio <= 0:
        velocidade_x = -velocidade_x

    if y + raio >= altura or y - raio <= 0:
        velocidade_y = -velocidade_y

    tela.fill(fundo)
    pygame.draw.circle(tela, bola, (x, y), raio)
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()