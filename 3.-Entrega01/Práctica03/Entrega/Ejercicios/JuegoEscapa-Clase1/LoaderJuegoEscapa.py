import functools
import itertools

from os import listdir
from os.path import isfile, join

def getAllLevels():
    mypath = 'levels/'
    onlyfiles = [f for f in listdir(mypath) if f.startswith(
        'level') and f.endswith('.txt') and isfile(join(mypath, f))]
    onlyfiles.sort()
    return onlyfiles

def getCodigoMapa(caracter):
    '''
    Devuelve el código de mapa asociado a cada caracter.
    '''
    codigo = 0
    if caracter == '-':
        codigo = 1
    elif caracter == '¡':
        codigo = 2
    elif caracter == '*':
        codigo = 3
    elif caracter == '!':
        codigo = 4
    elif caracter == '+':
        codigo = 5
    elif caracter == '@':
        codigo = 6

    return codigo

def getJuego(filename):
    '''
    Obtiene un juego a partir del archivo que lo codifica
    '''

    archivo = open(filename, "r", encoding="utf-8")
    lineas = archivo.readlines()

    # noMapa = set(['#','%']) # Aquí, identificas si la línea correspondiente no "pertenece" al Tablero.
    # Aquí, identificas si la línea correspondiente no "pertenece" al Tablero.
    noMapa = set([])
    # Aquí, generas una lista que tiene el valor de la longitud de cada línea, y obtienes el
    ancho = functools.reduce(max, map(len, lineas))-1
    # valor máximo de ellas, el cual "te determinará" el ancho de la matriz.

    mapa = []

    nFila = 0
    for linea in lineas:

        # Aquí generas una fila de ceros que, más abajo, irás rellenando "como corresponda".
        fila = list(itertools.repeat(0, ancho))

        nCol = 0
        for ch in linea:
            if ch == '\n':
                break

            codigo = getCodigoMapa(ch)
            fila[nCol] = codigo

            nCol += 1

        mapa.append(fila)
        nFila += 1

    return mapa