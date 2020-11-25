from os import listdir
from os.path import join, isfile
from pathlib import Path
from JuegoEscapa import State, Level
from typing import List


class Loader:
    """
    Clase utilizada para cargar niveles a partir de su representación en ficheros de texto
    """

    def __init__(self):
        self.file_element = {"#": ["wall", None],
                             "@": ["floor", "player"],
                             "+": ["floor", "rock"],
                             "*": ["floor", "target"],
                             "-": ["floor", "water"],
                             " ": ["floor", None],
                             "¡": ["floor", "key"],
                             "x": ["floor", "cross"],
                             "!": ["enemy", None]}

    def checks_conditions(self, file: str, levels_path: str) -> bool:
        """
        Comprueba que el archivo pasado cumpla ciertas condiciones.

        Args:
            file (str): Archivo a comprobar las condiciones.

        Returns:
            bool: El archivo cumple todas las condiciones.
        """
        return (
            file.endswith(".txt") and
            file.startswith("level") and
            isfile(join(levels_path, file)))

    def get_all_levels(self):
        """
        Obtiene la lista de niveles disponibles
        que son todos aquellos contenidos en la carpeta /levels/

        Args: 
        Ninguno

        Returns:
            List[str]: Lista de paths de todos los niveles.
        """
        abs_path = Path(__file__).parent
        levels_path = join(abs_path, "levels")

        levels = [file for file in listdir(
            levels_path) if self.checks_conditions(file, levels_path)]
        levels.sort()

        return levels

    def get_txt_level(self, level: str):
        """
        Abre el nivel pasado y lo lee para guardar el texto que hay en el.

        Args:
            level (str): Nivel a leer y sacar el texto.

        Returns:
            List[str]: Lista con cada fila de texto del nivel.
        """
        abs_path = Path(__file__).parent
        levels_path = join(abs_path, "levels")

        filename = join(levels_path, level)
        file_text = open(filename, "r", encoding="utf-8").read().split("\n")

        return file_text

    def load_level(self, level: List[str]):
        """
        Carga el nivel pasado como texto.

        Args:
            level (List[str]): Nivel en formato de texto-

        Returns:
           Tuple(Level, State) : Retorna el nivel y el estado según el nivel.
        """
        board: List[List[int]] = []
        target = ()
        enemies = set()

        player: List[int] = None
        key = ()
        rocks = set()
        water = set()
        crosses = set()

        player_has_key = False

        for i, line in enumerate(level):
            board_row: List[int] = []
            for j, char in enumerate(line):
                element: List[str] = self.file_element[char]
                if "floor" in element:
                    board_row.append(1)
                else:
                    board_row.append(0)

                if "player" in element:
                    player = [i, j]
                elif "rock" in element:
                    rocks.add((i, j))
                elif "water" in element:
                    water.add((i, j))
                elif "key" in element:
                    key = (i, j)
                elif "cross" in element:
                    crosses.add((i, j))
                elif "target" in element:
                    target = (i, j)
                elif "enemy" in element:
                    enemies.add((i, j))

            if board_row:
                board.append(tuple(board_row))

        board = tuple(board)

        return Level(board, target, enemies), State(player, rocks, water, crosses, key, player_has_key)
