import sys
import pygame

print("juego iniciado")
pygame.init()

#dimensiones de la pantalla del juego
dimensiones_pantalla = (1280, 720)
pantalla = pygame.display.set_mode(dimensiones_pantalla)

#función que halla la posición X de la imagen para
#que quede centrado horizontalmente en la ventana
def centrar_hztl(dimensionX_pantalla, dimensionX_imagen):
    return (dimensionX_pantalla - dimensionX_imagen)/2

#clase que se encarga de administrar las distintas pantallas
#que se van a mostrar cuando el usuario presiona un botón
class administrador_de_ventanas():
    def __init__(self):
        self.ventana = 'menu'

    def administrar(self):
        if self.ventana == 'menu':
            self.menu()

    def menu(self):
        #cierra el juego si presiona X de la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("juego cerrado")
                pygame.quit()
                sys.exit()
        
        #carga las siguientes imágenes
        boton_jugar = pygame.image.load("./assets/botones/jugar.png")
        boton_instr = pygame.image.load("./assets/botones/instrucciones.png")
        boton_salir = pygame.image.load("./assets/botones/salir.png")

        #posición X de los botones del menú
        posX_botones_menu = centrar_hztl(dimensiones_pantalla[0], 200)

        #agrega las imágenes previamente cargadas al menú
        pantalla.blit(boton_jugar, (posX_botones_menu, 300))
        pantalla.blit(boton_instr, (posX_botones_menu, 400))
        pantalla.blit(boton_salir, (posX_botones_menu, 500))

        pygame.display.update()
        if pygame.mouse.get_pressed()[0] == True:
            if posX_botones_menu <= pygame.mouse.get_pos()[0] <= posX_botones_menu + 200:
                if 500 <= pygame.mouse.get_pos()[1] <= 500 + 50:
                    self.salir()

    def salir(self):
        pygame.quit()
        sys.exit()

#programa principal
while True:
    ventana = administrador_de_ventanas()
    ventana.administrar()