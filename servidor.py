import socket
from _thread import *
zoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

zoc.bind(('localhost', 8080))

zoc.listen(2)

print("iniciado")
jugadores = 0

fila00 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fila01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila02 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila03 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila04 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila05 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila06 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila07 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila08 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila09 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tablero0 = [fila00, fila01, fila02, fila03, fila04, fila05, fila06, fila07, fila08, fila09]

fila10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fila11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila14 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila17 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila18 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fila19 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tablero1 = [fila10, fila11, fila12, fila13, fila14, fila15, fila16, fila17, fila18, fila19]
def hilo(cliente):
    global jugadores
    jugadores += 1
    cliente.send(str.encode("True"))
    booleano = 1
    while True:
        
        if booleano != 0:
            string = cliente.recv(2048).decode("utf-8").split(".")
            for j in range(10):
                for i in range(10):
                    tablero0[j][i] = int(string[j][1+i*3])
                print(tablero0[j])
            booleano = 0
        string = cliente.recv(2048).decode("utf-8")
        if string == 'desconectar':
            break
    
    print("cliente", jugadores, "ha desconectado.")
    jugadores -= 1
    cliente.close()

while True:
    (cliente, direccion) = zoc.accept()
    
    print(jugadores)

    start_new_thread(hilo, (cliente,))

