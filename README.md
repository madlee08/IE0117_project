# battleship-project
Un sencillo juego de batalla naval (Battleship) de dos jugadores escrito en [Python](https://www.python.org/) utilizando [Pygame](https://www.pygame.org/news) para un curso de programación. Adicionalmente se utiliza [PyInstaller](https://www.pyinstaller.org/) para poder crear los archivos ejecutables.

## Ejecutable
### Descarga del ejecutable
Si desea probar el juego sin tener que instalar Python ni Pygame, puede descargar el ejecutable en el siguiente enlace:
Sistema operativo | Archivo
----------------- | -------
Windows 10 64 bits | [cliente_win10_x64-1.0.2.zip](https://github.com/madlee08/battleship-project/releases/download/v1.0.2/cliente_win10_x64.zip)

Una vez descargado el archivo `.zip`, descomprima el archivo `.zip` en un directorio de su preferencia. Dentro de ese directorio debe aparecer `cliente_win10_x64`.
### Ejecución del juego
El archivo ejecutable que debe buscar es `battleship`, su ruta es `./cliente_win10_x64/battleship`. Una vez encontrado el archivo, ejecute dicho archivo. El juego debe abrirse.

## Código fuente
### Requisitos
Antes de descargar el código fuente, verifique que cumple los siguientes requisitos:
- Tener [Python 3.7.4](https://www.python.org/downloads/release/python-374/) instalado.
- Tener Pygame 1.9.6 instalado (ver la sección Instalación de Pygame 1.9.6).
- [Opcional] Si desea crear el archivo ejecutable, debe tener [PyInstaller](https://www.pyinstaller.org/downloads.html) instalado.

#### Instalación de Pygame 1.9.6
De acuerdo con [Pygame](https://www.pygame.org/wiki/GettingStarted), la mejor manera de instalar Pygame es usar `pip`. Entonces, siguiendo las instrucciones de Pygame, abra una terminal y ejecute el siguiente comando:

```shell
pip install -U pygame==1.9.6 --user
```

Se agrega `==1.9.6` para indicar que se desea instalar específicamente la versión 1.9.6 de Pygame.

### Descarga del código fuente
El código fuente se puede descargar aquí: [battleship-source.zip](https://github.com/madlee08/battleship-project/archive/main.zip). Debe descomprimir el archivo `.zip`.

Alternativamente se puede usar `git clone` para clonar este repositorio:
```shell
git clone https://github.com/madlee08/battleship-project.git
```

### Ejecución del código
Para ejecutar el código, ejecute el siguiente comando en la terminal:

```shell
py cliente.py
```
