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

class administrador_de_botones:
    def __init__(self):
        self.out = 'menu'
        self.btn_jugar = pygame.image.load("./assets/botones/jugar.png")
        self.btn_instr = pygame.image.load("./assets/botones/instrucciones.png")
        self.btn_salir = pygame.image.load("./assets/botones/salir.png")
        self.btn_regsr = pygame.image.load("./assets/botones/regresar.png")
        self.tablero = pygame.image.load("./assets/tablero/tablero_juego.png")
        self.negro = (0,0,0)

        self.dX_boton = 200
        self.dY_boton = 50

        self.pX_bmen = centrar_hztl(dimX_vent, self.dX_boton)
        self.pY_jugar = 300
        self.pY_instr = 400
        self.pY_salir = 500

        self.pX_regsr = 1000
        self.pY_regsr = 600

        self.pX_tablero = 50
        self.pY_tablero = 50

    def menu(self):
        pantalla.fill(self.negro)
        pantalla.blit(self.btn_jugar, (self.pX_bmen, self.pY_jugar))
        pantalla.blit(self.btn_instr, (self.pX_bmen, self.pY_instr))
        pantalla.blit(self.btn_salir, (self.pX_bmen, self.pY_salir))
        pygame.display.update()

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_bmen <= pX_mouse <= self.pX_bmen + self.dX_boton:
                if self.pY_jugar <= pY_mouse <= self.pY_jugar + self.dY_boton:
                    self.out = 'preparacion'

                if self.pY_salir <= pY_mouse <= self.pY_salir + self.dY_boton:
                    self.out = 'salir'

    def preparacion(self):
        pantalla.fill(self.negro)
        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))
        pantalla.blit(self.tablero, (self.pX_tablero, self.pY_tablero))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_regsr <= pX_mouse <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pY_mouse <= self.pY_regsr + self.dY_boton:
                    self.out = 'menu'

class administrador_de_barcos:
    def __init__(self):
        self.barco0 = pygame.image.load("./assets/barcos/0_x2.png")
        self.barco1 = pygame.image.load("./assets/barcos/1_x3.png")
        self.barco2 = pygame.image.load("./assets/barcos/2_x3.png")
        self.barco3 = pygame.image.load("./assets/barcos/3_x4.png")
        self.barco4 = pygame.image.load("./assets/barcos/4_x5.png")

        self.pX = [50, 290, 50, 50, 242]
        self.pY = [50, 146, 242, 338, 146]

        self.dX = [93, 141, 141, 189, 237]
        self.dY = [45, 45, 45, 45, 45]

        self.rotado = [False, False, False, False, True]

    def ubicar(self):
        if self.rotado[0] == True:
            rotado0 = pygame.transform.rotate(self.barco0, 90)
            pantalla.blit(rotado0, (self.pX[0], self.pY[0]))

        else:
            pantalla.blit(self.barco0, (self.pX[0], self.pY[0]))

        if self.rotado[1] == True:
            rotado1 = pygame.transform.rotate(self.barco1, 90)
            pantalla.blit(rotado1, (self.pX[1], self.pY[1]))

        else:
            pantalla.blit(self.barco1, (self.pX[1], self.pY[1]))

        if self.rotado[2] == True:
            rotado2 = pygame.transform.rotate(self.barco2, 90)
            pantalla.blit(rotado2, (self.pX[2], self.pY[2]))

        else:
            pantalla.blit(self.barco2, (self.pX[2], self.pY[2]))

        if self.rotado[3] == True:
            rotado3 = pygame.transform.rotate(self.barco3, 90)
            pantalla.blit(rotado3, (self.pX[3], self.pY[3]))

        else:
            pantalla.blit(self.barco3, (self.pX[3], self.pY[3]))

        if self.rotado[4] == True:
            rotado4 = pygame.transform.rotate(self.barco4, 90)
            pantalla.blit(rotado4, (self.pX[4], self.pY[4]))

        else:
            pantalla.blit(self.barco4, (self.pX[4], self.pY[4]))

        pygame.display.update()

    def rotar(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_der = pygame.mouse.get_pressed()[2]

        if clic_der == True:
            if self.rotado[0] == True:
                if self.pX[0] <= pX_mouse <= self.pX[0] + self.dY[0]:
                    if self.pY[0] <= pY_mouse <= self.pY[0] + self.dX[0]:
                        self.rotado[0] = False
                        time.sleep(0.2)

            else:
                if self.pX[0] <= pX_mouse <= self.pX[0] + self.dX[0]:
                    if self.pY[0] <= pY_mouse <= self.pY[0] + self.dY[0]:
                        self.rotado[0] = True
                        time.sleep(0.2)

            if self.rotado[1] == True:
                if self.pX[1] <= pX_mouse <= self.pX[1] + self.dY[1]:
                    if self.pY[1] <= pY_mouse <= self.pY[1] + self.dX[1]:
                        self.rotado[1] = False
                        time.sleep(0.2)

            else:
                if self.pX[1] <= pX_mouse <= self.pX[1] + self.dX[1]:
                    if self.pY[1] <= pY_mouse <= self.pY[1] + self.dY[1]:
                        self.rotado[1] = True
                        time.sleep(0.2)

            if self.rotado[2] == True:
                if self.pX[2] <= pX_mouse <= self.pX[2] + self.dY[2]:
                    if self.pY[2] <= pY_mouse <= self.pY[2] + self.dX[2]:
                        self.rotado[2] = False
                        time.sleep(0.2)

            else:
                if self.pX[2] <= pX_mouse <= self.pX[2] + self.dX[2]:
                    if self.pY[2] <= pY_mouse <= self.pY[2] + self.dY[2]:
                        self.rotado[2] = True
                        time.sleep(0.2)
            
            if self.rotado[3] == True:
                if self.pX[3] <= pX_mouse <= self.pX[3] + self.dY[3]:
                    if self.pY[3] <= pY_mouse <= self.pY[3] + self.dX[3]:
                        self.rotado[3] = False
                        time.sleep(0.2)

            else:
                if self.pX[3] <= pX_mouse <= self.pX[3] + self.dX[3]:
                    if self.pY[3] <= pY_mouse <= self.pY[3] + self.dY[3]:
                        self.rotado[3] = True
                        time.sleep(0.2)

            if self.rotado[4] == True:
                if self.pX[4] <= pX_mouse <= self.pX[4] + self.dY[4]:
                    if self.pY[4] <= pY_mouse <= self.pY[4] + self.dX[4]:
                        self.rotado[4] = False
                        time.sleep(0.2)

            else:
                if self.pX[4] <= pX_mouse <= self.pX[4] + self.dX[4]:
                    if self.pY[4] <= pY_mouse <= self.pY[4] + self.dY[4]:
                        self.rotado[4] = True
                        time.sleep(0.2)

class administrador_de_ventanas:
    def __init__(self):
        self.ventana = 'menu'
        self.botones = administrador_de_botones()
        self.barcos = administrador_de_barcos()

    def administrar(self):
        if self.ventana == 'menu':
            self.menu()
        if self.ventana == 'preparacion':
            self.preparacion()
        if self.ventana == 'salir':
            self.salir_menu()

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
        self.salir_x()
        self.botones.menu()
        self.ventana = self.botones.out

    def preparacion(self):
        self.salir_x()
        self.botones.preparacion()
        self.barcos.ubicar()
        self.barcos.rotar()
        self.ventana = self.botones.out

#programa principal
ventana = administrador_de_ventanas()
while True:
    ventana.administrar()