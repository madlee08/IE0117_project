import socket
from _thread import *

zoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

zoc.bind(('localhost', 8080))

jgd_max = 4
zoc.listen(jgd_max)

class administrador_estado:
    def __init__(self, max_jgd):
        self.max = int(max_jgd)
        self.num_jgd = 0
        self.jgd_ctd = []
        self.partida = []
        self.tableros = []

        for i in range(int(self.max/2)):
            self.partida.append(False)

        for i in range(self.max):
            self.jgd_ctd.append(0)
            self.tableros.append(list())
            for j in range(10):
                self.tableros[i].append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

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
                self.tableros[num_id][i][j] = int(str_tab.split("],", 10)[i][2+3*j])
    
    def tab_str(self, num_id):
        return str(self.tableros[num_id])

def hilo(cliente):
    global cont

    cont.incrementar()

    num_id = cont.ubicar_jgd()
    tab = cliente.recv(2048).decode("utf-8")

    cont.copiar(num_id, tab)

    print('cliente', num_id + 1, 'conectado')

    for i in range(10):
        print(cont.tableros[num_id][i])

    while True:
        # if (num_id % 2) == 0:
        #     cliente.send((str.encode(cont.tab_str(num_id+1))))

        # elif (num_id % 2) == 1:
        #     cliente.send((str.encode(cont.tab_str(num_id+1))))
        cliente.send((str.encode(cont.tab_str(num_id))))

        string = cliente.recv(2048).decode("utf-8")
        if string == 'desconectar':
            break
    cont.disminuir()
    cont.jgd_ctd[num_id] = 0
    print('cliente', num_id + 1, 'desconectado')
    cliente.close()

cont = administrador_estado(jgd_max)

while True:
    (cliente, direccion) = zoc.accept()
    start_new_thread(hilo, (cliente,))