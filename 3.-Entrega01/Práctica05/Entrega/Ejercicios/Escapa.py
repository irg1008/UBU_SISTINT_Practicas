"""
Las partes actualizables del juego como jugadores, agua y las cajas

Traduce comentarios al ingles
"""
class State:
    def __init__(self,player,piedra,agua,aspa,llave):
        """ Constructor por defecto

        Devuelve un objeto de tipo State

        Parámetros:
        jugador -- coordenadas del jugador en forma de lista
        cajas -- set de tuplas de coordenadas de las cajas
        """  
        self.player = player
        self.piedra = piedra
        self.agua = agua
        self.aspa = aspa
        self.llave = llave

        
    def get_player(self):
        """ Obtiene las coordenadas del jugador

        Devuelve lista con las coordenadas y,x del jugador

        Parámetros:
        Ninguno
        """   
        return self.player
    
    def get_piedra(self):
        """ Obtiene las coordenadas de las piedras

        Devuelve un set con y,x de cada una de las cajas, cada caja una tupla

        Parámetros:
        Ninguno
        """   
        return self.piedra
    
    
    def get_agua(self):
        """ Obtiene las coordenadas de las casillas con agua

        Devuelve un set con y,x de cada una de las cajas, cada caja una tupla

        Parámetros:
        Ninguno
        """   
        return self.agua
       
    
    def get_aspa(self):
        """ Obtiene las coordenadas de la casilla con el "aspa"

        Devuelve un set con y,x

        Parámetros:
        Ninguno
        """   
        return self.aspa
    
    
    def get_llave(self):
        """ Obtiene las coordenadas de la casilla con la llave

        Devuelve un set con y,x de cada una de las cajas, cada caja una tupla

        Parámetros:
        Ninguno
        """   
        return self.llave
    
    
    def __str__(self):
        """ Obtiene la representación del objeto 

        Devuelve un string con la representación del objeto

        Parámetros:
        Ninguno
        """   
        return str(self.player)+str(self.piedra)+str(self.agua)+str(self.aspa)+str(self.llave)
    
    
    def __repr__(self):
        """ Obtiene la representación del objeto 

        Devuelve un string con la representación del objeto

        Parámetros:
        Ninguno
        """  
        return str(self.player)+str(self.piedra)+str(self.agua)+str(self.aspa)+str(self.llave)
    
    def __eq__(self,other):
        return all([self.piedra == other.piedra,
                    self.agua == other.agua,
                    self.aspa == other.aspa,
                    self.llave == other.llave])
    
    
    def __hash__(self):
        return hash((str(self.player), frozenset(self.piedra), frozenset(self.agua), frozenset(self.aspa),frozenset(self.llave)))
    
    
"""
Define un nivel del juego

Las partes no-actualizables del juego como el el tablero y los destinos de cajas
"""    


class Level:
    
    def __init__(self,tablero,destino,enemigo):
        """ Constructor por defecto

        Devuelve un objeto de tipo Level

        Parámetros:
        tablero -- lista de listas (lista 2D) que representa casillas libres y muros
        destinos -- frozenset de tuplas de coordenadas de los destinos
        """  
        self.tablero = tablero
        self.destino = destino
        self.enemigo = enemigo
        
    def get_tablero(self):
        """ Devuelve el tablero

        Devuelve lista 2d, 0 en las posiciones libres, 1 en las posiciones donde hay un muro

        Parámetros:
        Ninguno
        """ 
        return self.tablero
    
    def get_destino(self):
        """ Obtiene las coordenadas de los destinos

        Devuelve un frozenset con y,x de cada una de los destinos, cada destino una tupla

        Parámetros:
        Ninguno
        """   
        return self.destino
    
    
    def get_enemigo(self):
        """ Obtiene las coordenadas de los destinos

        Devuelve un frozenset con y,x de cada una de los destinos, cada destino una tupla

        Parámetros:
        Ninguno
        """   
        return self.enemigo
    
    
    
    def __str__(self):
        """ Obtiene la representación del objeto 

        Devuelve un string con la representación del objeto

        Parámetros:
        Ninguno
        """   
        return str(self.tablero)+str(self.destino)+str(self.enemigo)
    
    
    
    def __repr__(self):
        """ Obtiene la representación del objeto 

        Devuelve un string con la representación del objeto

        Parámetros:
        Ninguno
        """   
        return str(self.tablero)+str(self.destino)+str(self.enemigo)
