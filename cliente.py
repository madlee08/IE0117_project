import pygame, sys, time

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
        self.btn_jugar = pygame.image.load("./assets/botones/jugar.png")
        self.btn_instr = pygame.image.load("./assets/botones/instrucciones.png")
        self.btn_salir = pygame.image.load("./assets/botones/salir.png")
        self.btn_regsr = pygame.image.load("./assets/botones/regresar.png")
        self.tablero = pygame.image.load("./assets/tablero/tablero_juego.png")
        self.barco0 = pygame.image.load("./assets/barcos/0_x2.png")
        self.barco1 = pygame.image.load("./assets/barcos/1_x3.png")
        self.barco2 = pygame.image.load("./assets/barcos/2_x3.png")
        self.barco3 = pygame.image.load("./assets/barcos/3_x4.png")
        self.barco4 = pygame.image.load("./assets/barcos/4_x5.png")

        self.dX_boton = 200
        self.dY_boton = 50
        
        self.pX_tablero = 50
        self.pY_tablero = 50

        self.pX_bmen = centrar_hztl(dimX_vent, self.dX_boton)
        self.pY_jugar = 300
        self.pY_instr = 400
        self.pY_salir = 500

        self.pX_regsr = 1000
        self.pY_regsr = 600
        
        self.pX_barco = [50, 50, 50, 50, 242]
        self.pY_barco = [50, 146, 242, 338, 146]
        
        self.dX_barco = [93, 141, 141, 189, 237]
        self.dY_barco = [45, 45, 45, 45, 45]

        self.rotado_barco = [False, False, False, False, True]

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

        pantalla.fill(self.negro)
        #agrega las imágenes previamente cargadas al menú
        pantalla.blit(self.btn_jugar, (self.pX_bmen, self.pY_jugar))
        pantalla.blit(self.btn_instr, (self.pX_bmen, self.pY_instr))
        pantalla.blit(self.btn_salir, (self.pX_bmen, self.pY_salir))

        pygame.display.update()
        if pygame.mouse.get_pressed()[0] == True:
            if self.pX_bmen <= pygame.mouse.get_pos()[0] <= self.pX_bmen + self.dX_boton:
                if self.pY_jugar <= pygame.mouse.get_pos()[1] <= self.pY_jugar + self.dY_boton:
                    self.ventana = 'preparacion'

                if self.pY_salir <= pygame.mouse.get_pos()[1] <= self.pY_salir + self.dY_boton:
                    self.salir_menu()

    def preparacion(self):
        self.salir_x()

        pantalla.fill(self.negro)

        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))
        pantalla.blit(self.tablero, (self.pX_tablero, self.pY_tablero))
        self.ubicarbarcos()
        self.rotarbarcos()

        if pygame.mouse.get_pressed()[0] == True:
            if self.pX_regsr <= pygame.mouse.get_pos()[0] <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pygame.mouse.get_pos()[1] <= self.pY_regsr + self.dY_boton:
                    self.ventana = 'menu'

    def ubicarbarcos(self):
        if self.rotado_barco[0] == True:
            rotado0 = pygame.transform.rotate(self.barco0, 90)
            pantalla.blit(rotado0, (self.pX_barco[0], self.pY_barco[0]))

        else:
            pantalla.blit(self.barco0, (self.pX_barco[0], self.pY_barco[0]))
        
        if self.rotado_barco[1] == True:
            rotado1 = pygame.transform.rotate(self.barco1, 90)
            pantalla.blit(rotado1, (self.pX_barco[1], self.pY_barco[1]))

        else:
            pantalla.blit(self.barco1, (self.pX_barco[1], self.pY_barco[1]))
        
        if self.rotado_barco[2] == True:
            rotado2 = pygame.transform.rotate(self.barco2, 90)
            pantalla.blit(rotado2, (self.pX_barco[2], self.pY_barco[2]))

        else:
            pantalla.blit(self.barco2, (self.pX_barco[2], self.pY_barco[2]))

        if self.rotado_barco[3] == True:
            rotado3 = pygame.transform.rotate(self.barco3, 90)
            pantalla.blit(rotado3, (self.pX_barco[3], self.pY_barco[3]))

        else:
            pantalla.blit(self.barco3, (self.pX_barco[3], self.pY_barco[3]))

        if self.rotado_barco[4] == True:
            rotado4 = pygame.transform.rotate(self.barco4, 90)
            pantalla.blit(rotado4, (self.pX_barco[4], self.pY_barco[4]))

        else:
            pantalla.blit(self.barco4, (self.pX_barco[4], self.pY_barco[4]))

        pygame.display.update()
    def rotarbarcos(self):
        if pygame.mouse.get_pressed()[2] == True:
            if self.rotado_barco[0] == True:
                if self.pX_barco[0] <= pygame.mouse.get_pos()[0] <= self.pX_barco[0] + self.dY_barco[0]:
                    if self.pY_barco[0] <= pygame.mouse.get_pos()[1] <= self.pY_barco[0] + self.dX_barco[0]:
                        self.rotado_barco[0] = False
                        time.sleep(0.25)

            else:
                if self.pX_barco[0] <= pygame.mouse.get_pos()[0] <= self.pX_barco[0] + self.dX_barco[0]:
                    if self.pY_barco[0] <= pygame.mouse.get_pos()[1] <= self.pY_barco[0] + self.dY_barco[0]:
                        self.rotado_barco[0] = True
                        time.sleep(0.25)

#programa principal
ventana = administrador_de_ventanas()
while True:
    ventana.administrar()