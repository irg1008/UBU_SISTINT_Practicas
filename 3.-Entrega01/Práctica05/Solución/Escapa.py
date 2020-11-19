"""
Las partes actualizables del juego como jugadores, agua y piedra(s)

"""
class State:
    def __init__(self,player,piedra,agua,aspa,llave):
        """ Constructor por defecto

        Devuelve un objeto de tipo State

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

        Devuelve un set con y,x de cada una de las piedras, cada piedra es una tupla

        Parámetros:
        Ninguno
        """   
        return self.piedra
    
    
    def get_agua(self):
        """ Obtiene las coordenadas de las casillas con agua        

        Parámetros:
        Ninguno
        """   
        return self.agua
       
    
    def get_aspa(self):
        """ Obtiene las coordenadas de la casilla con el "aspa"

        Parámetros:
        Ninguno
        """   
        return self.aspa
    
    
    def get_llave(self):
        """ Obtiene las coordenadas de la casilla con la llave

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

Las partes no-actualizables del juego como el el tablero y el/los destino(s)
"""    


class Level:
    
    def __init__(self,tablero,destino,enemigo):
        """ Constructor por defecto

        Devuelve un objeto de tipo Level

        Parámetros:
        tablero -- Representa casillas libres y muros
        destinos 
        enemigo(s)
        """  
        self.tablero = tablero
        self.destino = destino
        self.enemigo = enemigo
        
        
    def get_tablero(self):
        """ Devuelve el tablero       

        Parámetros:
        Ninguno
        """ 
        return self.tablero
    
    
    def get_destino(self):
        """ Obtiene las coordenadas del (de los) destino(s)        

        Parámetros:
        Ninguno
        """   
        return self.destino
    
    
    
    def get_enemigo(self):
        """ Obtiene las coordenadas del enemigo

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
