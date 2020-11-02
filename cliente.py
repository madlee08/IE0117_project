import pygame, sys, time


print("juego iniciado")
pygame.init()


#dimensiones de la pantalla del juego
dX_vent = 1280
dY_vent = 720
pantalla = pygame.display.set_mode((dX_vent, dY_vent))


#función que halla la posición X de la imagen para
#que quede centrado horizontalmente en la ventana
def centrar_hztl(dimensionX_pantalla, dimensionX_imagen):
    return (dimensionX_pantalla - dimensionX_imagen)/2

class administrador_de_imagenes:
    def __init__(self):
        self.tablero = pygame.image.load("./assets/tablero/tablero_juego.png")
        self.ayuda = pygame.image.load("./assets/texto/ayuda.png")
        self.instr = pygame.image.load("./assets/texto/instrucciones.png")
        self.pX_tablero = 50
        self.pY_tablero = 50
        self.pX_ayuda = 750
        self.pY_ayuda = 100
        self.pX_instr = 160
        self.pY_instr = 50

        self.azul = (0 ,88,122)
    
    def menu(self):
        pantalla.fill(self.azul)
    
    def preparacion(self):
        pantalla.fill(self.azul)
        pantalla.blit(self.tablero, (self.pX_tablero, self.pY_tablero))
        pantalla.blit(self.ayuda, (self.pX_ayuda, self.pY_ayuda))

    def instrucciones(self):
        pantalla.fill(self.azul)
        pantalla.blit(self.instr, (self.pX_instr, self.pY_instr))


class administrador_de_botones:
    def __init__(self):
        self.out = 'menu'
        self.btn_jugar = pygame.image.load("./assets/botones/jugar.png")
        self.btn_instr = pygame.image.load("./assets/botones/instrucciones.png")
        self.btn_salir = pygame.image.load("./assets/botones/salir.png")
        self.btn_regsr = pygame.image.load("./assets/botones/regresar.png")
        self.btn_bscar = pygame.image.load("./assets/botones/buscar.png")

        self.dX_boton = 200
        self.dY_boton = 50

        self.pX_bmen = centrar_hztl(dX_vent, self.dX_boton)
        self.pY_jugar = 300
        self.pY_instr = 400
        self.pY_salir = 500

        self.pX_regsr = 1000
        self.pY_regsr = 600

        self.pX_bscar = 750
        self.pY_bscar = 600

    def menu(self):
        pantalla.blit(self.btn_jugar, (self.pX_bmen, self.pY_jugar))
        pantalla.blit(self.btn_instr, (self.pX_bmen, self.pY_instr))
        pantalla.blit(self.btn_salir, (self.pX_bmen, self.pY_salir))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_bmen <= pX_mouse <= self.pX_bmen + self.dX_boton:
                if self.pY_jugar <= pY_mouse <= self.pY_jugar + self.dY_boton:
                    self.out = 'preparacion'

                if self.pY_instr <= pY_mouse <= self.pY_instr + self.dY_boton:
                    self.out = 'instrucciones'

                if self.pY_salir <= pY_mouse <= self.pY_salir + self.dY_boton:
                    self.out = 'salir'

    def preparacion(self):
        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))
        pantalla.blit(self.btn_bscar, (self.pX_bscar, self.pY_bscar))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_regsr <= pX_mouse <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pY_mouse <= self.pY_regsr + self.dY_boton:
                    self.out = 'menu'

    def instrucciones(self):
        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_regsr <= pX_mouse <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pY_mouse <= self.pY_regsr + self.dY_boton:
                    self.out = 'menu'

class administrador_de_barcos:
    def __init__(self):
        self.b0 = pygame.image.load("./assets/barcos/0_x2.png")
        self.b1 = pygame.image.load("./assets/barcos/1_x3.png")
        self.b2 = pygame.image.load("./assets/barcos/2_x3.png")
        self.b3 = pygame.image.load("./assets/barcos/3_x4.png")
        self.b4 = pygame.image.load("./assets/barcos/4_x5.png")

        self.barco = [self.b0, self.b1, self.b2, self.b3, self.b4]

        self.pX = [434, 50, 386, 338, 290]
        self.pY = [434, 386, 386, 338, 290]

        self.dX = [93, 141, 141, 189, 237]
        self.dY = [45, 45, 45, 45, 45]

        self.rotado = [False, False, False, False, False]

    def ubicar(self):
        for i in range(5):
            if self.rotado[i] == True:
                pantalla.blit(pygame.transform.rotate(self.barco[i], 90), (self.pX[i], self.pY[i]))

            else:
                pantalla.blit(self.barco[i], (self.pX[i], self.pY[i]))

    def rotar(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_der = pygame.mouse.get_pressed()[2]

        if clic_der == True:
            for i in range(5):
                if self.rotado[i] == True:
                    if self.pX[i] <= pX_mouse <= self.pX[i] + self.dY[i]:
                        if self.pY[i] <= pY_mouse <= self.pY[i] + self.dX[i]:
                            self.rotado[i] = False
                            time.sleep(0.2)

                else:
                    if self.pX[i] <= pX_mouse <= self.pX[i] + self.dX[i]:
                        if self.pY[i] <= pY_mouse <= self.pY[i] + self.dY[i]:
                            self.rotado[i] = True
                            time.sleep(0.2)

    def trasladar(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            for i in range(5):
                if self.rotado[i] == True:
                    if self.pX[i] <= pX_mouse <= self.pX[i] + self.dY[i]:
                        if self.pY[i] <= pY_mouse <= self.pY[i] + self.dX[i]:
                            self.pX[i] = pX_mouse - self.dY[i]/2
                            self.pY[i] = pY_mouse - self.dX[i]/2

                else:
                    if self.pX[i] <= pX_mouse <= self.pX[i] + self.dX[i]:
                        if self.pY[i] <= pY_mouse <= self.pY[i] + self.dY[i]:
                            self.pX[i] = pX_mouse - self.dX[i]/2
                            self.pY[i] = pY_mouse - self.dY[i]/2

    def limitar(self):
        lim_inf = 50
        olim_sup = [434, 386, 386, 338, 290]
        plim_sup = 482

        for i in range(5):
            if self.rotado[i] == True:
                if self.pX[i] < lim_inf:
                    self.pX[i] = lim_inf
                if self.pX[i] > plim_sup:
                    self.pX[i] = plim_sup
                
                if self.pY[i] < lim_inf:
                    self.pY[i] = lim_inf
                if self.pY[i] > olim_sup[i]:
                    self.pY[i] = olim_sup[i]
            
            else:
                if self.pX[i] < lim_inf:
                    self.pX[i] = lim_inf
                if self.pX[i] > olim_sup[i]:
                    self.pX[i] = olim_sup[i]

                if self.pY[i] < lim_inf:
                    self.pY[i] = lim_inf
                if self.pY[i] > plim_sup:
                    self.pY[i] = plim_sup

    def ajustar(self):
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == False:
            for i in range(10):
                for j in range(5):
                    if 50+47*i <= self.pX[j] <= 50 + 47*(i+1):
                        self.pX[j] = 50+48*i

                    if 50+47*i <= self.pY[j] <= 50 + 47*(i+1):
                        self.pY[j] = 50+48*i


class administrador_de_ventanas:
    def __init__(self):
        self.ventana = 'menu'
        self.imagenes_fondo = administrador_de_imagenes()
        self.botones = administrador_de_botones()
        self.barcos = administrador_de_barcos()

    def administrar(self):
        if self.ventana == 'menu':
            self.menu()
        if self.ventana == 'preparacion':
            self.preparacion()
        if self.ventana == 'instrucciones':
            self.instrucciones()
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
        self.imagenes_fondo.menu()
        self.botones.menu()
        pygame.display.update()
        self.ventana = self.botones.out

    def preparacion(self):
        self.salir_x()
        self.imagenes_fondo.preparacion()
        self.botones.preparacion()
        self.barcos.ubicar()
        self.barcos.rotar()
        self.barcos.trasladar()
        self.barcos.limitar()
        self.barcos.ajustar()
        pygame.display.update()
        self.ventana = self.botones.out
    
    def instrucciones(self):
        self.salir_x()
        self.imagenes_fondo.instrucciones()
        self.botones.instrucciones()
        pygame.display.update()
        self.ventana = self.botones.out


#programa principal
ventana = administrador_de_ventanas()
while True:
    ventana.administrar()