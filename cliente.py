import pygame, sys, time, socket


print("juego iniciado")
pygame.init()
pygame.mixer.quit()
pygame.font.quit()

reloj = pygame.time.Clock()
#dimensiones de la pantalla del juego
dX_vent = 1280
dY_vent = 720
pantalla = pygame.display.set_mode((dX_vent, dY_vent))


#función que halla la posición X de la imagen para
#que quede centrado horizontalmente en la ventana
def centrar(dim_pantalla, dim_imagen):
    return (dim_pantalla - dim_imagen)/2

# -----------------------------------------------------------------------------------------------------------------------------
# Posiciones X y Y de la imagen de fondo
pX_fondo = 0
pY_fondo = 0

# -----------------------------------------------------------------------------------------------------------------------------
# Constantes de la seccion de menu

# Botones
JGR_mu = 0 # Jugar
INS_mu = 1 # Instrucciones
CRD_mu = 2 # Creditos
SLR_mu = 3

# Dimensiones X (dX) y Y (dY) y posiciones X (pX) y Y (dY) de los botones de la seccion del menu
# Orden de los elementos de las listas: [0] Jugar, [1] Instrucciones, [2] Creditos, [3] Salir
dX_btn_mu = [200, 200, 0, 200]
dY_btn_mu = [50, 50, 0, 50]

pX_btn_mu = [centrar(dX_vent, dX_btn_mu[JGR_mu]), centrar(dX_vent, dX_btn_mu[INS_mu]), 0, centrar(dX_vent, dX_btn_mu[SLR_mu])]
pY_btn_mu = [300, 400, 0, 500]

# -----------------------------------------------------------------------------------------------------------------------------
# Constantes de la seccion de instrucciones

# Botones
RGS_in = 0 # Regresar

# Textos
TXI_in = 0 # Instrucciones

# Dimensiones X (dX) y Y (dY) y posiciones X (pX) y Y (dY) de los botones de la seccion instrucciones
# Orden de los elementos de las listas: [0] Regresar
dX_btn_in = [200]
dY_btn_in = [50]

pX_btn_in = [1050]
pY_btn_in = [650]

# Posiciones X (pX) y Y (dY) de los textos de la seccion del instrucciones
# Orden de los elementos de las listas: [0] Instrucciones
pX_txt_in = [160]
pY_txt_in = [50]

# -----------------------------------------------------------------------------------------------------------------------------
# Constantes de la seccion de preparacion

# Botones
RST_pr = 0 # Reset
BSR_pr = 1 # Buscar rival
RGS_pr = 2 # Regresar

# Textos
TXI_pr = 0 # Instrucciones

# Tableros
TAJ_pr = 0 # Jugador

# Dimensiones X (dX) y Y (dY) y posiciones X (pX) y Y (dY) de los botones de la seccion de preparacion
# Orden de los elementos de las listas: [0] Reset, [1] Buscar rival, [2] Regresar
dX_btn_pr = [200, 200, 200]
dY_btn_pr = [50, 50, 50]

pX_btn_pr = [0, 800, 1050]
pY_btn_pr = [0, 650, 650]

# Posiciones X (pX) y Y (dY) de los textos de la seccion de preparacion
# Orden de los elementos de las listas: [0] Instrucciones
pX_txt_pr = [750]
pY_txt_pr = [100]

# Posiciones X (pX) y Y (dY) de los tableros de la seccion de preparacion
# Orden de los elementos de las listas: [0] Jugador
pX_tab_pr = [50]
pY_tab_pr = [50]

# -----------------------------------------------------------------------------------------------------------------------------
# Constantes de la seccion en partida 

# Botones
RGS_pt = 0 # Regresar

# Tableros
TAJ_pt = 0 # Jugador
TAR_pt = 1 # Rival

# Textos
CRG_pt = 0 # Buscando rival

# Dimensiones X (dX) y Y (dY) y posiciones X (pX) y Y (dY) de los botones de la seccion en partida
# Orden de los elementos de las listas: [0] Regresar
dX_btn_pt = [200]
dY_btn_pt = [50]

pX_btn_pt = [1050]
pY_btn_pt = [650]

# Posiciones X (pX) y Y (dY) de los tableros de la seccion en partida
# Orden de los elementos de las listas: [0] Jugador, [1] Rival
pX_tab_pt = [50, 600]
pY_tab_pt = [50, 50]

# Posiciones X (pX) y Y (dY) de los textos de la seccion en partida
# Orden de los elementos de las listas: [0] Buscando rival
pX_txt_pt = [pX_tab_pt[TAR_pt]]
pY_txt_pt = [pY_tab_pt[TAR_pt]]

# rutas relativa de los imagenes
ruta_fondo = "./assets/fondo/pixel_art_bg.png"

ruta_btn_jgr = "./assets/botones/jugar.png"
ruta_btn_ins = "./assets/botones/instrucciones.png"
ruta_btn_slr = "./assets/botones/salir.png"
ruta_btn_rgs = "./assets/botones/regresar.png"
ruta_btn_bsr = "./assets/botones/buscar.png"

ruta_txt_ins = "./assets/texto/instrucciones.png"
ruta_txt_ayd = "./assets/texto/ayuda.png"
ruta_txt_crg = "./assets/texto/carga.png"

ruta_tab_jgd = "./assets/tablero/tablero_azul.png"
ruta_tab_rvl = "./assets/tablero/tablero_blanco.png"

# cargador de imagenes de pygame
png_fondo = pygame.image.load(ruta_fondo).convert_alpha()

png_btn_jgr = pygame.image.load(ruta_btn_jgr).convert_alpha()
png_btn_ins = pygame.image.load(ruta_btn_ins).convert_alpha()
png_btn_slr = pygame.image.load(ruta_btn_slr).convert_alpha()
png_btn_rgs = pygame.image.load(ruta_btn_rgs).convert_alpha()
png_btn_bsr = pygame.image.load(ruta_btn_bsr).convert_alpha()

png_txt_ins = pygame.image.load(ruta_txt_ins).convert_alpha()
png_txt_ayd = pygame.image.load(ruta_txt_ayd).convert_alpha()
png_txt_crg = pygame.image.load(ruta_txt_crg).convert_alpha()

png_tab_jgd = pygame.image.load(ruta_tab_jgd).convert_alpha()
png_tab_rvl = pygame.image.load(ruta_tab_rvl).convert_alpha()

# llave para entrar al servidor
KEY = "fd4mCbapCLhgPdNr82dSyLdRGL7DUNZMzREdgVxDupyEn73T3xv2mpKRyDSpMMfAscB6eAhZ2DWNfUtfcz2j4JdGuj9YkbQmyNwLjwcesxTj3Jj8LRdfHKuE48kA65jR"
# dX_btn_prep = []

# dX_btn_part = []

# dX_btn_inst = []
# dX_btn_fin = []


class administrador_de_botones:
    def __init__(self):
        self.vent = 'menu'
        self.tablero_rival = []
        self.tiros_jugador = []
        self.tiros_rival = []
        self.celdas = 0

        for i in range(10):
            self.tablero_rival.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.tiros_rival.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.tiros_jugador.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    btn_regsr = png_btn_rgs

    actdo = pygame.image.load("./assets/tablero/acertado.png")
    agua = pygame.image.load("./assets/tablero/agua.png")

    tiro_r = pygame.image.load("./assets/tablero/rival.png")

    dX_boton = 200
    dY_boton = 50

    pX_bmen = centrar(dX_vent, dX_boton)

    pY_fin = 500

    pX_tablero = 600
    pY_tablero = 50

    def menu(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if pX_btn_mu[JGR_mu] <= pX_mouse <= pX_btn_mu[JGR_mu] + dX_btn_mu[JGR_mu]:
                if pY_btn_mu[JGR_mu] <= pY_mouse <= pY_btn_mu[JGR_mu] + dY_btn_mu[JGR_mu]:
                    self.vent = 'preparacion'

            if pX_btn_mu[INS_mu] <= pX_mouse <= pX_btn_mu[INS_mu] + dX_btn_mu[INS_mu]:
                if pY_btn_mu[INS_mu] <= pY_mouse <= pY_btn_mu[INS_mu] + dY_btn_mu[INS_mu]:
                    self.vent = 'instrucciones'

            if pX_btn_mu[SLR_mu] <= pX_mouse <= pX_btn_mu[SLR_mu] + dX_btn_mu[SLR_mu]:
                if pY_btn_mu[SLR_mu] <= pY_mouse <= pY_btn_mu[SLR_mu] + dY_btn_mu[SLR_mu]:
                    self.vent = 'salir'

    def instrucciones(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if pX_btn_in[RGS_in] <= pX_mouse <= pX_btn_in[RGS_in] + dX_btn_in[RGS_in]:
                if pY_btn_in[RGS_in] <= pY_mouse <= pY_btn_in[RGS_in] + dY_btn_in[RGS_in]:
                    self.vent = 'menu'

    def preparacion(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if pX_btn_pr[RGS_pr] <= pX_mouse <= pX_btn_pr[RGS_pr] + dX_btn_pr[RGS_pr]:
                if pY_btn_pr[RGS_pr] <= pY_mouse <= pY_btn_pr[RGS_pr] + dY_btn_pr[RGS_pr]:
                    self.vent = 'menu'
            
            if pX_btn_pr[BSR_pr] <= pX_mouse <= pX_btn_pr[BSR_pr] + dX_btn_pr[BSR_pr]:
                if pY_btn_pr[BSR_pr] <= pY_mouse <= pY_btn_pr[BSR_pr] + dY_btn_pr[BSR_pr]:
                    self.vent = 'juego'

    def juego(self):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if pX_btn_pt[RGS_pt] <= pX_mouse <= pX_btn_pt[RGS_pt] + dX_btn_pt[RGS_pt]:
                if pY_btn_pt[RGS_pt] <= pY_mouse <= pY_btn_pt[RGS_pt] + dY_btn_pt[RGS_pt]:
                    self.vent = 'preparacion'
                    for j in range(10):
                        for i in range(10):
                            self.tiros_jugador[j][i] = 0
                    time.sleep(0.2)

    def resultado(self):
        pantalla.blit(self.btn_regsr, (self.pX_bmen, self.pY_fin))

        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True:
            if self.pX_bmen <= pX_mouse <= self.pX_bmen + self.dX_boton:
                if self.pY_fin <= pY_mouse <= self.pY_fin + self.dY_boton:
                    self.vent = 'menu'
                    for j in range(10):
                        for i in range(10):
                            self.tiros_jugador[j][i] = 0
                    time.sleep(0.2)

    def clic(self, turno):
        pX_mouse = pygame.mouse.get_pos()[0]
        pY_mouse = pygame.mouse.get_pos()[1]
        clic_izq = pygame.mouse.get_pressed()[0]

        if clic_izq == True and turno == True:
            for j in range(10):
                for i in range(10):
                    if self.tiros_jugador[j][i] != 1:
                        if self.pX_tablero + 48*i <= pX_mouse <= self.pX_tablero + 48*(i+1):
                            if self.pY_tablero + 48*j <= pY_mouse <= self.pY_tablero + 48*(j+1):
                                self.tiros_jugador[j][i] = 1
                                time.sleep(0.2)
                                return False

    def update_tiros_j(self):
        for j in range(10):
                for i in range(10):
                    if self.tiros_jugador[j][i] != 0:
                        if self.tablero_rival[j][i] != 0:
                            pantalla.blit(self.actdo, (self.pX_tablero + 48*i, self.pY_tablero + 48*j))
                        else:
                            pantalla.blit(self.agua, (self.pX_tablero + 48*i, self.pY_tablero + 48*j))

    def update_tiros_r(self):
        for j in range(10):
                for i in range(10):
                    if self.tiros_rival[j][i] != 0:
                        pantalla.blit(self.tiro_r, (50 + 48*i, 50 + 48*j))

    def copiar_tab_r(self, de_tablero):
        for i in range(10):
            self.tablero_rival[i] = de_tablero[i]
    
    def copiar_tiros_r(self, de_tablero):
        for i in range(10):
            self.tiros_rival[i] = de_tablero[i]
    
    def reset(self):
        for i in range(10):
            for j in range(10):
                self.tiros_rival[i][j] = 0

    def revisar_tiros(self):
        self.celdas = 0
        for i in range(10):
            for j in range(10):
                if self.tiros_jugador[i][j] == 1 and self.tablero_rival[i][j] != 0:
                    self.celdas += 1

    def quedan_barcos(self):
        if self.celdas != 17:
            return True
        else:
            return False


class administrador_de_imagenes:
    gana = pygame.image.load("./assets/texto/ganado.png")
    pierde = pygame.image.load("./assets/texto/perdido.png")
    fin = pygame.image.load("./assets/fondo/fin.png").convert_alpha()

    turno_jugador = pygame.image.load("./assets/texto/turno_jugador.png")
    turno_rival = pygame.image.load("./assets/texto/turno_rival.png")

    pX_fin = centrar(dX_vent, 600)
    pY_fin = centrar(dY_vent, 400)
    
    def menu(self):
        pantalla.blit(png_fondo, (pX_fondo, pY_fondo))
        pantalla.blit(png_btn_jgr, (pX_btn_mu[JGR_mu], pY_btn_mu[JGR_mu]))
        pantalla.blit(png_btn_ins, (pX_btn_mu[INS_mu], pY_btn_mu[INS_mu]))
        pantalla.blit(png_btn_slr, (pX_btn_mu[SLR_mu], pY_btn_mu[SLR_mu]))
    
    def instrucciones(self):
        pantalla.blit(png_fondo, (pX_fondo, pY_fondo))
        pantalla.blit(png_btn_rgs, (pX_btn_in[RGS_in], pY_btn_in[RGS_in]))
        pantalla.blit(png_txt_ins, (pX_txt_in[TXI_in], pY_txt_in[TXI_in]))

    def preparacion(self):
        pantalla.blit(png_fondo, (pX_fondo, pY_fondo))
        pantalla.blit(png_btn_rgs, (pX_btn_pr[RGS_pr], pY_btn_pr[RGS_pr]))
        pantalla.blit(png_btn_bsr, (pX_btn_pr[BSR_pr], pY_btn_pr[BSR_pr]))
        pantalla.blit(png_tab_jgd, (pX_tab_pr[TAJ_pr], pY_tab_pr[TAJ_pr]))
        pantalla.blit(png_txt_ayd, (pX_txt_pr[TXI_pr], pY_tab_pr[TXI_pr]))

    def juego(self, en_partida, turno):
        pantalla.blit(png_fondo, (pX_fondo, pY_fondo))
        pantalla.blit(png_btn_rgs, (pX_btn_pt[RGS_pt], pY_btn_pt[RGS_pt]))
        pantalla.blit(png_tab_jgd, (pX_tab_pt[TAJ_pt], pY_tab_pt[TAJ_pt]))
        pantalla.blit(png_tab_rvl, (pX_tab_pt[TAR_pt], pY_tab_pt[TAR_pt]))
        if en_partida == 1:
            pantalla.blit(png_txt_crg,(pX_txt_pt[CRG_pt], pY_txt_pt[CRG_pt]))
        else:
            if turno == True:
                pantalla.blit(self.turno_jugador, (50, 550))
            if turno == False:
                pantalla.blit(self.turno_rival, (40, 550))

    def resultado(self, estado):
        pantalla.blit(self.fin, (self.pX_fin, self.pY_fin))
        if estado == 1:
            pantalla.blit(self.gana, (400, 300))
        if estado == 2:
            pantalla.blit(self.pierde, (400, 300))
        if estado == 3:
            pantalla.blit(self.gana, (400, 300))



class administrador_de_barcos:

    b0 = pygame.image.load("./assets/barcos/0_x2.png")
    b1 = pygame.image.load("./assets/barcos/1_x3.png")
    b2 = pygame.image.load("./assets/barcos/2_x3.png")
    b3 = pygame.image.load("./assets/barcos/3_x4.png")
    b4 = pygame.image.load("./assets/barcos/4_x5.png")

    barco = [b0, b1, b2, b3, b4]

    def __init__(self):
        self.tablero_jugador = []

        self.pX = [434, 50, 386, 338, 290]
        self.pY = [434, 386, 386, 338, 290]

        self.dX = [93, 141, 141, 189, 237]
        self.dY = [45, 45, 45, 45, 45]

        self.rotado = [False, False, False, False, False]

        for i in range(10):
            self.tablero_jugador.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

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

    def rvs_celda(self):
        for j in range(10):
            for i in range(10):
                px_clr = pantalla.get_at((51+48*i, 51+48*j))

                if px_clr == (1, 74, 7, 255):
                    self.tablero_jugador[j][i] = 1

                elif px_clr == (139, 85 , 8, 255):
                    self.tablero_jugador[j][i] = 2

                elif px_clr == (17, 89, 88, 255):
                    self.tablero_jugador[j][i] = 3

                elif px_clr == (140, 144, 13, 255):
                    self.tablero_jugador[j][i] = 4

                elif px_clr == (201, 95, 45, 255):
                    self.tablero_jugador[j][i] = 5

                else:
                    self.tablero_jugador[j][i] = 0

    def administrar(self):
        self.rotar()
        self.trasladar()
        self.limitar()
        self.ajustar()
        self.ubicar()
        self.rvs_celda()


class red:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.enviado = False
        self.tablero_jugador = []
        self.tiros_jugador = []
        self.tiros_rival = []
        self.tablero_rival = []
        self.voo = 1
        self.turno = False
        self.fin = 0
        self.quedan_barcos = True

        for i in range(10):
            self.tablero_jugador.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.tiros_jugador.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.tablero_rival.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            self.tiros_rival.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def copiar_tab_j(self, de_tablero):
        for i in range(10):
            self.tablero_jugador[i] = de_tablero[i]

    def copiar_tiros_j(self, de_tablero):
        for i in range(10):
            self.tiros_jugador[i] = de_tablero[i]

    def conectar(self):
        if self.enviado == False:
            self.cliente.connect(('35.226.60.53', 8080))
            self.cliente.send(str.encode(KEY))
            time.sleep(1)
            self.cliente.send(str.encode(str(self.tablero_jugador)))
            print(len(str(self.tablero_jugador)))
            self.enviado = True
        
        if self.quedan_barcos == False:
                self.cliente.send(str.encode("terminar"))

        else:
            if self.voo == 0 and self.turno == False:
                self.cliente.send(str.encode(str(self.tiros_jugador)))
                print(len(str(self.tiros_jugador)))
            else:
                self.cliente.send(str.encode("dummy"))

        if self.fin == 0:
            string = self.cliente.recv(2048).decode("utf-8")
        
        if string[0] == '[' and self.voo == 1:
            for i in range(10):
                for j in range(10):
                    self.tablero_rival[i][j] = int(string.split("],", 9)[i][2+3*j])
            self.voo = 0
            print(string)

        if (string[0] == 'T' or string[0] == 'F') and self.voo == 0:
            booleano, tab = string.split(".", 1)
            if booleano == 'True':
                self.turno = True

                for i in range(10):
                    for j in range(10):
                        self.tiros_rival[i][j] = int(tab.split("],", 9)[i][2+3*j])

        if string == 'rivaldc':
            self.fin = 3
            self.voo = 1
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if string == 'gana':
            self.fin = 1
            self.voo = 1
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if string == 'pierde':
            self.fin = 2
            self.voo = 1
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def desconectar(self, booleano):
        if booleano == 1:
            self.cliente.send(str.encode('desconectar'))
            self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class administrador_de_ventanas:
    def __init__(self):
        self.imagenes = administrador_de_imagenes()
        self.botones = administrador_de_botones()
        self.barcos = administrador_de_barcos()
        self.red = red()
        self.booleano = 0
        self.booleano2 = 1
        self.booleano3 = 1
        self.booleano4 = 1
    def salir_x(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.botones.vent == 'juego':
                    self.red.desconectar(1)
                print("juego cerrado X")
                pygame.quit()
                sys.exit()

    def salir_menu(self):
        print("juego cerrado MENU")
        pygame.quit()
        sys.exit()

    def menu(self):
        self.imagenes.menu()
        self.botones.menu()
        self.booleano3 = 1
        self.red.fin = 0


    def preparacion(self):
        self.imagenes.preparacion()
        self.botones.preparacion()
        self.barcos.administrar()
        if self.booleano == 1:
            self.red.desconectar(self.booleano)
            self.red.enviado = False
            self.red.voo = 1
            self.booleano2 = 1
            self.booleano4 = 1
            self.botones.reset()
            self.botones.celdas = 0
            self.booleano = 0

    def juego(self):
        self.booleano = 1
        self.imagenes.juego(self.red.voo, self.red.turno)
        self.botones.juego()
        self.barcos.ubicar()
        if self.booleano2 == 1:
            self.barcos.rvs_celda()
            self.red.copiar_tab_j(self.barcos.tablero_jugador)
            self.booleano2 = 0

        self.red.copiar_tiros_j(self.botones.tiros_jugador)
        self.red.conectar()

        if self.red.voo == 0:
            if self.booleano4 == 1:
                self.botones.copiar_tab_r(self.red.tablero_rival)
                self.booleano4 = 0
            seleccionado = self.botones.clic(self.red.turno)
            self.red.turno = seleccionado
            self.botones.copiar_tiros_r(self.red.tiros_rival)
            self.botones.update_tiros_r()
            self.botones.update_tiros_j()
            self.botones.revisar_tiros()
            quedan = self.botones.quedan_barcos()
            self.red.quedan_barcos = quedan

        if self.red.fin != 0:
            self.botones.vent = 'fin'

    def resultado(self):
        if self.booleano3 == 1:
            self.booleano = 0
            self.red.fin = 0
            self.red.enviado = False
            self.red.voo = 1
            self.botones.celdas = 0
            self.booleano3 = 0
        self.botones.reset()
        turno = self.red.turno
        self.imagenes.juego(0, turno)
        self.barcos.ubicar()
        self.botones.update_tiros_j()
        resultado = self.red.fin
        self.imagenes.resultado(resultado)
        self.botones.resultado()

    
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

        if self.botones.vent == 'fin':
            self.resultado()

        if self.botones.vent == 'salir':
            self.salir_menu()

#programa principal
ventana = administrador_de_ventanas()
while True:
    ventana.administrar()
    pygame.display.update()
    reloj.tick(60)