import socket
from _thread import *
zoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

zoc.bind(('localhost', 8080))

jgd_max = 4
zoc.listen(jgd_max)

jgd_ctd = []
partida = []
tableros = []

for i in range(int(jgd_max/2)):
    jgd_ctd.append(0)
    jgd_ctd.append(0)
    partida.append(False)

for i in range(10):
    fila = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    tablero = []
    for j in range(10):
        tablero.append(fila)
    tableros.append(tablero)

def hilo(cliente):
    global jgd_ctd
    num_id = -1
    for i in range(jgd_max):
        if jgd_ctd[i] == 0:
            jgd_ctd[i] = 1
            num_id = i
            break
    print('cliente', num_id + 1, 'conectado')
    cliente.send(str.encode("True"))

    booleano = 1
    while True:
        if booleano != 0:
            string = cliente.recv(2048).decode("utf-8").split(".")
            for j in range(10):
                for i in range(10):
                    tableros[num_id][j][i] = int(string[j][1+i*3])
                print(tableros[num_id][j])
            cliente.send((str.encode(".".join(str(x) for x in tableros[num_id+1]))))
            booleano = 0
        
        string = cliente.recv(2048).decode("utf-8")

        if string == 'desconectar':
            break
    jgd_ctd[num_id] = 0
    print('cliente', num_id + 1, 'desconectado')
    cliente.close()

print("iniciado")
while True:
    (cliente, direccion) = zoc.accept()
    start_new_thread(hilo, (cliente, ))
    
