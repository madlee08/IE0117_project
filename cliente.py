import pygame, sys, time, socket


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


class administrador_de_botones:
    def __init__(self):
        self.vent = 'menu'
        self.fila0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila1 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.fila3 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.fila4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.tablero = [self.fila0, self.fila1, self.fila2, self.fila3, self.fila4, self.fila5, self.fila6, self.fila7, self.fila8, self.fila9]

    btn_jugar = pygame.image.load("./assets/botones/jugar.png")
    btn_instr = pygame.image.load("./assets/botones/instrucciones.png")
    btn_salir = pygame.image.load("./assets/botones/salir.png")
    btn_regsr = pygame.image.load("./assets/botones/regresar.png")
    btn_bscar = pygame.image.load("./assets/botones/buscar.png")

    actdo = pygame.image.load("./assets/tablero/acertado.png")

    dX_boton = 200
    dY_boton = 50

    pX_bmen = centrar_hztl(dX_vent, dX_boton)
    pY_jugar = 300
    pY_instr = 400
    pY_salir = 500

    pX_regsr = 1050
    pY_regsr = 650

    pX_bscar = 800
    pY_bscar = 650

    pX_tablero = 600
    pY_tablero = 50
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
                    self.vent = 'preparacion'

                if self.pY_instr <= pY_mouse <= self.pY_instr + self.dY_boton:
                    self.vent = 'instrucciones'

                if self.pY_salir <= pY_mouse <= self.pY_salir + self.dY_boton:
                    self.vent = 'salir'

    def preparacion(self):
        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))
        pantalla.blit(self.btn_bscar, (self.pX_bscar, self.pY_bscar))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_regsr <= pX_mouse <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pY_mouse <= self.pY_regsr + self.dY_boton:
                    self.vent = 'menu'
            
            if self.pX_bscar <= pX_mouse <= self.pX_bscar + self.dX_boton:
                if self.pY_bscar <= pY_mouse <= self.pY_bscar + self.dY_boton:
                    self.vent = 'juego'

    def juego(self):
        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_regsr <= pX_mouse <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pY_mouse <= self.pY_regsr + self.dY_boton:
                    self.vent = 'preparacion'
                    for j in range(10):
                        for i in range(10):
                            self.tablero[j][i] = 0
                    time.sleep(0.2)

    def clic(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            for j in range(10):
                for i in range(10):
                    if self.pX_tablero + 48*i <= pX_mouse <= self.pX_tablero + 48*(i+1):
                        if self.pY_tablero + 48*j <= pY_mouse <= self.pY_tablero + 48*(j+1) :
                            self.tablero[j][i] = 1

    def actualizar_celda(self):
        for j in range(10):
                for i in range(10):
                    if self.tablero[j][i] != 0:
                            pantalla.blit(self.actdo, (self.pX_tablero + 48*i, self.pY_tablero + 48*j))

    def instrucciones(self):
        pantalla.blit(self.btn_regsr, (self.pX_regsr, self.pY_regsr))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_regsr <= pX_mouse <= self.pX_regsr + self.dX_boton:
                if self.pY_regsr <= pY_mouse <= self.pY_regsr + self.dY_boton:
                    self.vent = 'menu'


class administrador_de_imagenes:
    tablero_a = pygame.image.load("./assets/tablero/tablero_azul.png")
    tablero_b = pygame.image.load("./assets/tablero/tablero_blanco.png")
    ayuda = pygame.image.load("./assets/texto/ayuda.png")
    instr = pygame.image.load("./assets/texto/instrucciones.png")
    pX_tablero = 50
    pY_tablero = 50
    pX_ayuda = 750
    pY_ayuda = 100
    pX_instr = 160
    pY_instr = 50

    azul = (0 ,88,122)
    
    def menu(self):
        pantalla.fill(self.azul)
    
    def preparacion(self):
        pantalla.fill(self.azul)
        pantalla.blit(self.tablero_a, (self.pX_tablero, self.pY_tablero))
        pantalla.blit(self.ayuda, (self.pX_ayuda, self.pY_ayuda))

    def juego(self):
        pantalla.fill(self.azul)
        pantalla.blit(self.tablero_a, (self.pX_tablero, self.pY_tablero))
        pantalla.blit(self.tablero_b, (600, 50))

    def instrucciones(self):
        pantalla.fill(self.azul)
        pantalla.blit(self.instr, (self.pX_instr, self.pY_instr))


class administrador_de_barcos:

    b0 = pygame.image.load("./assets/barcos/0_x2.png")
    b1 = pygame.image.load("./assets/barcos/1_x3.png")
    b2 = pygame.image.load("./assets/barcos/2_x3.png")
    b3 = pygame.image.load("./assets/barcos/3_x4.png")
    b4 = pygame.image.load("./assets/barcos/4_x5.png")

    barco = [b0, b1, b2, b3, b4]

    def __init__(self):
        self.fila0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.fila9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.tablero0 = [self.fila0, self.fila1, self.fila2, self.fila3, self.fila4, self.fila5, self.fila6, self.fila7, self.fila8, self.fila9]

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
                            self.pY[i] = pY_mouse - self.dX[i]/8

                else:
                    if self.pX[i] <= pX_mouse <= self.pX[i] + self.dX[i]:
                        if self.pY[i] <= pY_mouse <= self.pY[i] + self.dY[i]:
                            self.pX[i] = pX_mouse - self.dX[i]/8
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

    def administrar(self):
        self.rotar()
        self.trasladar()
        self.limitar()
        self.ajustar()
        self.ubicar()

    def rvs_celda(self):
        for j in range(10):
            for i in range(10):
                px_clr = pantalla.get_at((51+48*i, 51+48*j))

                if px_clr == (1, 74, 7, 255):
                    self.tablero0[j][i] = 1

                elif px_clr == (139, 85 , 8, 255):
                    self.tablero0[j][i] = 2

                elif px_clr == (17, 89, 88, 255):
                    self.tablero0[j][i] = 3

                elif px_clr == (140, 144, 13, 255):
                    self.tablero0[j][i] = 4

                elif px_clr == (201, 95, 45, 255):
                    self.tablero0[j][i] = 5

                else:
                    self.tablero0[j][i] = 0
            #print temporal para ver que la matriz esté en orden
            # print("{} ".format(self.tablero0[j]))


class red:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.enviado = False
        self.tablero = []

    def copiar(self, de_tablero):
        for i in range(10):
            self.tablero.append(de_tablero[i])

    def verificar(self, ventana):
        if ventana != 'juego':
            self.enviado = False

    def conectar(self):
        
        if self.enviado == False:
            self.cliente.connect(('localhost', 8080))
            self.cliente.send((str.encode(".".join(str(x) for x in self.tablero))))
            self.enviado = bool(self.cliente.recv(2048).decode("utf-8"))

    def desconectar(self, booleano, ventana):
        if booleano == 1 and ventana != 'juego':
            self.cliente.send((str.encode('desconectar')))
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class administrador_de_ventanas:
    def __init__(self):
        self.imagenes = administrador_de_imagenes()
        self.botones = administrador_de_botones()
        self.barcos = administrador_de_barcos()
        self.red = red()
        self.booleano = 0

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
        self.imagenes.menu()
        self.botones.menu()


    def preparacion(self):
        self.imagenes.preparacion()
        self.botones.preparacion()
        self.barcos.administrar()
        if self.booleano == 1:
            self.red.desconectar(self.booleano, self.botones.vent)
            self.booleano = 0

    def juego(self):
        self.booleano = 1
        self.imagenes.juego()
        self.botones.juego()
        self.barcos.ubicar()
        self.barcos.rvs_celda()
        self.red.copiar(self.barcos.tablero0)
        self.red.conectar()
        self.red.verificar(self.botones.vent)
        self.botones.clic()
        self.botones.actualizar_celda()

    
    def instrucciones(self):
        self.imagenes.instrucciones()
        self.botones.instrucciones()


    def administrar(self):
        self.salir_x()
        if self.botones.vent == 'menu':
            self.menu()

        if self.botones.vent == 'preparacion':
            self.preparacion()

        if self.botones.vent == 'instrucciones':
            self.instrucciones()

        if self.botones.vent == 'juego':
            self.juego()

        if self.botones.vent == 'salir':
            self.salir_menu()

#programa principal
ventana = administrador_de_ventanas()
while True:
    ventana.administrar()
    pygame.display.update()