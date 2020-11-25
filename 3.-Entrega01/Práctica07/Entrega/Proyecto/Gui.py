from ipywidgets import HTML, Dropdown, Button, HBox, VBox
from JuegoEscapa import Level, State, StaticObject, LevelBoard


class Gui:
    """
    Clase que define los componentes gráficos de la interfaz

    """
    def __init__(self, manual=True):
        """
        Constructor por defecto.
        Devuelve un objeto que crea la interfaz de usuario.

        Args:
            manual (bool, optional): Crea la interfaz para modo manual, false crea para modo automático. Defaults to True.
        """
        self.manual = manual
        self.image_element = {
            "floor": "./sprites/floor.png",
            "wall": "./sprites/wall.png",
            "target": "./sprites/target.png",
            "player": "./sprites/player.png",
            "rock": "./sprites/rock.png",
            "water": "./sprites/water.png",
            "key": "./sprites/key.png",
            "enemy": "./sprites/enemy.png",
            "cross": "./sprites/cross.gif"
        }

        viewfinder = HTML()
        dropdown = Dropdown(description="Choose Level:")

        up = Button(description="^")
        down = Button(description="v")
        right = Button(description=">")
        left = Button(description="<")
        empty = Button(description=" ")
        empty.margin = 2
        directions = VBox([HBox([empty, up]), HBox([left, down, right])])

        actions = self.get_actions()
        control = VBox([directions, actions])

        self.ui = VBox(children=[dropdown, viewfinder, control])

    def is_floor(self, board: LevelBoard, coord: StaticObject) -> bool:
        """
        Devuelve si la coordenada es suelo en el tablero pasado.

        Args:
            board (LevelBoard): Tablero.
            coord (StaticObject): Coordenada.

        Returns:
            bool: True si la coordenada pasada es suelo.
        """
        try:
            x, y = coord
            return board[x][y] == 1
        except IndexError:
            return False

    def get_content(self, level: Level, state: State, coord: StaticObject) -> StaticObject:
        """
        Obtiene el contenido de una determinada posición.

        Args:
            level (Level): Nivel.
            state (State): Estado.
            coord (StaticObject): Posición [y,x] de la que queremos conocer el contenido

        Returns:
            StaticObject: [description]
        """

        coord = tuple(coord)
        content = [None, None]

        board = level.get_board()
        target = level.get_target()
        enemies = level.get_enemies()
        rocks = state.get_rocks()
        water = state.get_water()
        key = state.get_key()
        crosses = state.get_crosses()
        player = state.get_player()

        # Floor/Wall/Target.
        if coord == target:
            content[0] = ("target")
        elif self.is_floor(board, coord):
            content[0] = ("floor")
        else:
            content[0] = ("wall")

        # Objects.
        if coord in rocks:
            content[1] = ("rock")
        elif coord in water:
            content[1] = ("water")
        elif coord in crosses:
            content[1] = ("cross")
        elif coord == key:
            content[1] = ("key")

        # Character.
        if list(coord) == player:
            content[1] = ("player")
        elif coord in enemies:
            content[1] = ("enemy")

        return tuple(content)

    def get_ui_elements(self) -> VBox:
        """
        Obtiene los componentes gráficos del juego.
        
        Returns:
            VBox: Contenedor con los botones, y el visor del juego.
        """
        return self.ui

    def get_actions(self) -> HBox:
        """
        Devuelve los botones de acción.

        Returns:
            HBox: Botones de acción 
                    - En modo manual solo: reiniciar
                    - En modo automático: reiniciar, resolver, sig, anterior
        """
        action_buttons = []

        reset = Button(description="Reset")
        action_buttons.append(reset)

        if not self.manual:
            resolve = Button(description="Resolve")
            next = Button(description="Next")
            previous = Button(description="Previous")
            action_buttons.append(resolve)
            action_buttons.append(next)
            action_buttons.append(previous)

        actions = HBox(action_buttons)
        return actions

    def get_html(self, level: Level, state: State) -> str:
        """
        Obtiene la representación gráfica del juego en formato HTML.

        Args:
            level (Level): Nivel.
            state (State): Estado.

        Returns:
            str: Juego en HTML.
        """
        height, width = level.get_board_sizes()

        new_row = "<tr>"
        end_row = "</tr>"

        html_string = "<style> img.game {width: 50px !important; height: 50px !important;}</style><table>"

        for i in range(height):
            html_string += new_row
            for j in range(width):
                content = self.get_content(level, state, (i, j))
                if not content[1]:
                    drawing = self.image_element[content[0]]
                else:
                    drawing = self.image_element[content[1]]
                html_string += f'<td><img class="game" src={drawing} alt=""></img></td>'
            html_string += end_row
        html_string += "</table>"

        return html_string
