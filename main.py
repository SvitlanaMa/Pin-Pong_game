import pygame

pygame.init()

scr_width = 500
scr_height = 500
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Ping Pong")
# создаём таймер
clock = pygame.time.Clock()

FPS = 50

screen.fill((20, 180, 255))

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()
    clock.tick(FPS)
