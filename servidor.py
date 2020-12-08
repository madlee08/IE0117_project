# Autores: Olger Ramírez Delgado, Mike Mai Chen y Anthony Monestel Guzmán.
# Este código está bajo la licencia de MIT.

import socket, time
from _thread import *

# Numero maximo de jugadores concurrentes
JGD_MAX = 20

# Numero de puerto
PUERTO = 8080

# Llave para dejar entrar al cliente
KEY = "fd4mCbapCLhgPdNr82dSyLdRGL7DUNZMzREdgVxDupyEn73T3xv2mpKRyDSpMMfAscB6eAhZ2DWNfUtfcz2j4JdGuj9YkbQmyNwLjwcesxTj3Jj8LRdfHKuE48kA65jR"


zoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

zoc.bind((socket.gethostname(), PUERTO))

zoc.listen()


class administrador_estado:
    def __init__(self, max_jgd):
        self.max = int(max_jgd)
        self.num_jgd = 0
        self.jgd_ctd = []
        self.partida = []
        self.tableros = []
        self.tiros = []
        self.turno = []

        for i in range(int(self.max/2)):
            self.partida.append(False)
            self.turno.append(0)

        for i in range(self.max):
            self.jgd_ctd.append(0)
            self.tableros.append(list())
            self.tiros.append(list())
            for j in range(10):
                self.tableros[i].append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                self.tiros[i].append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def incrementar(self):
        self.num_jgd += 1
    
    def disminuir(self):
        self.num_jgd -= 1

    def ubicar_jgd(self):
        for i in range(self.max):
            if self.jgd_ctd[i] == 0:
                self.jgd_ctd[i] = 1
                return i
                break

    def copiar(self, num_id, str_tab):
        for i in range(10):
            for j in range(10):
                self.tableros[num_id][i][j] = int(str_tab.split("],", 9)[i][2+3*j])
    
    def copiar_tiros(self, num_id, str_tab):
        for i in range(10):
            for j in range(10):
                self.tiros[num_id][i][j] = int(str_tab.split("],", 9)[i][2+3*j])
    
    def tab_str(self, num_id):
        return str(self.tableros[num_id])

    def listo(self, num_id):
        if (num_id % 2) == 0:
            if self.jgd_ctd[num_id + 1] == 1:
                return True
            else:
                return False

        else:
            if self.jgd_ctd[num_id - 1] == 1:
                return True
            else:
                return False

def hilo(cliente):
    key = cliente.recv(2048).decode("utf-8")

    if key == KEY:
        global cont

        cont.incrementar()
        num_id = cont.ubicar_jgd()

        tab = cliente.recv(2048).decode("utf-8")

        cont.copiar(num_id, tab)

        print(time.asctime())
        print('cliente', num_id + 1, 'conectado.', cont.num_jgd, 'jugadores conectados.')

        for i in range(10):
            print(cont.tableros[num_id][i])

        partida_lista = False

        while True:
            if cont.listo(num_id) == True:
                if partida_lista == False:
                    if (num_id % 2) == 0:
                        cliente.send(str.encode(cont.tab_str(num_id+1)))

                    else:
                        cliente.send(str.encode(cont.tab_str(num_id-1)))

                    cont.partida[int(num_id/2)] = True
                    partida_lista = True

                if partida_lista == True:
                    if (num_id % 2) == 0:
                        string = str(cont.tiros[num_id+1])

                        if  cont.turno[int(num_id/2)] == 0:
                            cliente.send(str.encode("True." + string))

                        else:
                            cliente.send(str.encode("False." + string))

                    else:
                        string2 = str(cont.tiros[num_id-1])

                        if  cont.turno[int(num_id/2)] == 1:
                            cliente.send(str.encode("True." + string2))

                        else:
                            cliente.send(str.encode("False." + string2))       

            else:
                cliente.send(str.encode("dummy"))


            string = cliente.recv(2048).decode("utf-8")

            if string[0] == '[':
                cont.copiar_tiros(num_id, string)

                if (num_id % 2) == 0:
                    cont.turno[int(num_id/2)] = 1

                else:
                    cont.turno[int(num_id/2)] = 0

            if string == 'desconectar':
                break

            if string == 'terminar':
                if cont.turno[int(num_id/2)] == 0:
                    if (num_id % 2) == 0:
                        cliente.send(str.encode("gana"))

                    else:
                        cliente.send(str.encode("pierde"))

                else:
                    if (num_id % 2) == 1:
                        cliente.send(str.encode("gana"))

                    else:
                        cliente.send(str.encode("pierde"))

                time.sleep(0.8)
                break

            if cont.partida[int(num_id/2)] == True:
                if cont.listo(num_id) == False:
                    cont.partida[int(num_id/2)] = False
                    cliente.send(str.encode("rivaldc"))
                    time.sleep(0.8)
                    break

        cont.disminuir()
        cont.jgd_ctd[num_id] = 0

        for i in range(10):
            cont.tiros[num_id][i]  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        print(time.asctime())
        print('cliente', num_id + 1, 'desconectado.', cont.num_jgd, 'jugadores conectados.')

    cliente.close()

cont = administrador_estado(JGD_MAX)

print(time.asctime())
print("servidor iniciado")


while True:
    (cliente, direccion) = zoc.accept()
    start_new_thread(hilo, (cliente,))