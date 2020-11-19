from ipywidgets import HTML, Dropdown ,Button, HBox, VBox, Box

"""
Clase que define los componentes gráficos de la interfaz

"""
class gui:
    
    
    def __init__(self, manual=True):
        """ Constructor por defecto

        Devuelve un objeto que crea la interfaz de usuario

        Parámetros:
        manual -- True (defecto) crea la interfaz para modo manual, false crea para modo automático
        """ 
        self.manual = manual
        self.element_image = {"suelo": "./sprites/suelo.jpg",
                              "pared": "./sprites/pared.jpg",
                              "destino": "./sprites/puerta.jpg",
                              "player": "./sprites/jugadorH.jpg",
                              "piedra": "./sprites/piedra.jpg",
                              "agua": "./sprites/agua.jpg",
                              "llave": "./sprites/llave.jpg",
                              "enemigo": "./sprites/enemigo.jpg",
                              "aspa": "./sprites/aspaprohibido.jpg"}
        
        
        # visor HTML donde se representará el juego
        visor=HTML()

        # Crea un desplegable con los niveles
        desplegable = Dropdown(description = 'Elija nivel:')

        # Botones para las direcciones
        up = Button(description="^")
        down = Button(description="v")
        right = Button(description=">")
        left = Button(description="<")
        cambia = Button(description="Change")

        empty=Button(description=" ")
        empty.margin=2
        
        

        #direcciones=VBox([HBox([empty,up,cambia]),HBox([left,down,right])])
        direcciones=VBox([HBox([empty,up]),HBox([left,down,right])])
        acciones = self.get_actions()
        
        control = VBox([direcciones,acciones])
        
        self.ui=VBox(children=[desplegable, visor, control])
        
        
        
    def get_content(self,level,state,coord):
        """
        Obtiene el contenido de una determinada posición

        Parameters
        ----------
        coord : Posición [y,x] de la que queremos conocer el contenido

        Returns
        --------
        contenido : Una lista de tamaño 2 con el elemento del nivel y del estado en la coordenada
        """
        content = [None,None]
        
        
        tablero = level.get_tablero()
        destino =level.get_destino()
        
        enemigo =level.get_enemigo()
        
        piedra = state.get_piedra()
        agua = state.get_agua()
        llave = state.get_llave()
        
        aspa = state.get_aspa()
        
        player = state.get_player()
                
        
        if coord == destino:
            content[0] = "destino"
        elif tablero[coord[0]][coord[1]] == 1:
            content[0] = "suelo"
        #elif tablero[coord[0]][coord[1]] == 2:
        #    content[0] = "enemigo"
        else:
            content[0] = "pared"
        
        if coord in piedra:
            content[1] = "piedra"
        
        if coord in agua:
            content[1] = "agua"
        
        if coord in aspa:
            content[1] = "aspa"
        
        if coord in llave:
            content[1] = "llave"
            
        if list(coord) == player:
            content[1] = "player"
        
        if coord == enemigo:
            content[0] = "enemigo"
                
    
        return content
        
        

    def get_ui_elements(self):
        """ Obtiene los componentes gráficos del juego

        Devuelve un contenedor con los botones, y el visor del juego
        
        Parámetros: 
        Ninguno
        """       
        

        return self.ui
    
    def get_actions(self):
        """         
        devuelve los botones de acción 
         en modo manual solo: reiniciar
         en modo automático: reiniciar, resolver, sig, anterior
        
        Parámetros: 
        Ninguno
        """       
        
        botones_accion = []
       
        reiniciar = Button(description="Reiniciar")
        botones_accion.append(reiniciar)
        
        if not self.manual:    
            
            resolver = Button(description="Resolver")
            siguiente = Button(description="Siguiente")
            anterior = Button(description="Anterior")
            botones_accion.append(resolver)
            botones_accion.append(siguiente)
            botones_accion.append(anterior)
            
            
        accciones = HBox(botones_accion)
        
        return accciones


    def get_html(self,level,state):
        """ 
        Obtiene la representación gráfica del juego en formato HTML

        Parámetros: 
        level- un nivel
        state - un estado
        """

        tablero = level.get_tablero()
        height = len(tablero)
        width = len(tablero[0])

        



        html_string = "<style> img.game {width: 50px !important; height: 50px !important;}</style><table>"



        new_row = "<tr>"
        end_row = "</tr>"

        for i in range(height):
            html_string+=new_row
            for j in range(width):

                content = self.get_content(level,state,(i,j))
                if content[1] is None:
                    drawing = self.element_image[content[0]]
                else:
                    drawing = self.element_image[content[1]]
                html = '<td><img class="game" src=%s alt=""></img></td>' % drawing     


                html_string+=html
            html_string+=end_row

        html_string += "</table>"


        return html_string



