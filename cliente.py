import sys
import pygame

print("juego iniciado")
pygame.init()

#dimensiones de la pantalla del juego
dimX_vent = 1280
dimY_vent = 720
pantalla = pygame.display.set_mode((dimX_vent, dimY_vent))

#función que halla la posición X de la imagen para
#que quede centrado horizontalmente en la ventana
def centrar_hztl(dimensionX_pantalla, dimensionX_imagen):
    return (dimensionX_pantalla - dimensionX_imagen)/2

#clase que se encarga de administrar las distintas pantallas
#que se van a mostrar cuando el usuario presiona un botón
class administrador_de_ventanas():
    def __init__(self):
        self.ventana = 'menu'
        self.boton_jugar = pygame.image.load("./assets/botones/jugar.png")
        self.boton_instr = pygame.image.load("./assets/botones/instrucciones.png")
        self.boton_salir = pygame.image.load("./assets/botones/salir.png")
        self.boton_regresar = pygame.image.load("./assets/botones/regresar.png")

        self.tablero = pygame.image.load("./assets/tablero/tablero_juego.png")

        self.dimX_boton = 200
        self.dimY_boton = 50

        self.negro = (0,0,0)

    def administrar(self):
        if self.ventana == 'menu':
            self.menu()
        if self.ventana == 'preparacion':
            self.preparacion()

    def salir_x(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("juego cerrado")
                pygame.quit()
                sys.exit()

    def salir_menu(self):
        pygame.quit()
        sys.exit()

    def menu(self):
        #cierra el juego si presiona X de la ventana
        self.salir_x()

        #posición X de los botones del menú
        posX = centrar_hztl(dimX_vent, self.dimX_boton)

        posY_jugar = 300
        posY_instr = 400
        posY_salir = 500

        pantalla.fill(self.negro)
        #agrega las imágenes previamente cargadas al menú
        pantalla.blit(self.boton_jugar, (posX, posY_jugar))
        pantalla.blit(self.boton_instr, (posX, posY_instr))
        pantalla.blit(self.boton_salir, (posX, posY_salir))

        pygame.display.update()
        if pygame.mouse.get_pressed()[0] == True:
            if posX <= pygame.mouse.get_pos()[0] <= posX + self.dimX_boton:
                if posY_jugar <= pygame.mouse.get_pos()[1] <= posY_jugar + self.dimY_boton:
                    self.ventana = 'preparacion'

                if posY_salir <= pygame.mouse.get_pos()[1] <= posY_salir + self.dimY_boton:
                    self.salir_menu()

    def preparacion(self):
        self.salir_x()

        pantalla.fill(self.negro)

        posX_regresar = 1000
        posY_regresar = 600

        pantalla.blit(self.boton_regresar, (posX_regresar, posY_regresar))
        pantalla.blit(self.tablero, (50, 50))

        pygame.display.update()

        if pygame.mouse.get_pressed()[0] == True:
            if posX_regresar <= pygame.mouse.get_pos()[0] <= posX_regresar + self.dimX_boton:
                if posY_regresar <= pygame.mouse.get_pos()[1] <= posY_regresar + self.dimY_boton:
                    self.ventana = 'menu'


#programa principal
ventana = administrador_de_ventanas()
while True:
    ventana.administrar()