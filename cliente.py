import sys
import pygame

print("juego iniciado")
pygame.init()

dimensiones = 800, 600
pantalla = pygame.display.set_mode(dimensiones)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("juego cerrado")
            sys.exit()