from os import listdir
from os.path import isfile, join

from Escapa import Level, State

"""
Clase utilizada para cargar niveles a partir de su representación en ficheros de texto

"""
class Loader:
    
    def __init__(self):
    
        self.file_element = {"#": ['pared', None],
                             "@": ['suelo', 'player'],
                             "+": ['suelo', 'piedra'],
                             "*": ['destino', None],
                             "-": ['suelo', 'agua'],
                             " ": ['suelo', None],
                             "¡": ['suelo', 'llave'],
                             "x": ['suelo', 'aspa'],
                             "!": ['enemigo', None]}
    
    
    def get_all_levels(self):
        """ Obtiene la lista de niveles disponibles
        que son todos aquellos contenidos en la carpeta /levels/

        Devuelve una lista con los manejadores a ficheros contenidos en la carpeta de niveles 
        
        Parámetros: 
        Ninguno
        """
        
        mypath='./levels/'
        onlyfiles = [f for f in listdir(mypath) if f.startswith('level') and f.endswith('.txt') and isfile(join(mypath, f))]
        onlyfiles.sort()
        return onlyfiles
    
    
    def load_level(self,str_level):
        """ Carga un nivel a partir de un texto

        Devuelve un objeto de tipo State y otro de tipo Level
        
        Parámetros: 
        str_level - un string con la codificación del nivel
        """
        
        level = str_level.split("\n")
    
        tablero = []
        piedra = set()
        agua = set()
        llave = set()
        destino = ()
        enemigo = ()
        aspa = set()

        player = None
    
        i =0
        for row in level:
            tablero_row = []
            j =0
            for caracter in row:
                element = self.file_element[caracter]

                if element[0] == "pared":
                    tablero_row.append(0)
                    
                elif element[0] == "enemigo":
                    tablero_row.append(0)
                    
                else:
                    tablero_row.append(1)

                if element[1] =="player":
                    player = [i,j]                

                if element[1] =="piedra":
                    piedra.add((i,j))

                if element[1] =="agua":
                    agua.add((i,j))
                    
                if element[1] =="llave":
                    llave.add((i,j))
                    
                if element[1] =="aspa":
                    aspa.add((i,j))

                if element[0] == "destino":
                    destino = (i,j)
                    
                if element[0] == "enemigo":
                    enemigo = (i,j)
                    

                j+=1
            i+=1
            if tablero_row:
                tablero.append(tuple(tablero_row))
    

        return Level(tablero,destino,enemigo),State(player,piedra,agua,aspa,llave)
    
