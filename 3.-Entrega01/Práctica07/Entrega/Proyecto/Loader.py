from os import listdir
from os.path import join, isfile
from pathlib import Path

from JuegoEscapa import State, Level


class Loader:
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

    def get_all_levels(self):
        abs_path = Path(__file__).parent
        levels_path = join(abs_path, "levels")

        def checks_conditions(file):
            return (
                file.endswith(".txt") and
                file.startswith("level") and
                isfile(join(levels_path, file)))

        levels = [file for file in listdir(
            levels_path) if checks_conditions(file)]
        levels.sort()

        return levels

    def get_txt_level(self, level):
        abs_path = Path(__file__).parent
        levels_path = join(abs_path, "levels")

        filename = join(levels_path, level)

        return open(filename, "r", encoding="utf-8").read().split("\n")

    def load_level(self, level):
        player = None
        board = []
        target = ()
        enemy = set()

        rocks = set()
        water = set()
        keys = set()
        crosses = set()

        player_has_key = False

        for i, line in enumerate(level):
            board_row = []
            for j, char in enumerate(line):
                element = self.file_element[char]
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
                    keys.add((i, j))
                elif "cross" in element:
                    crosses.add((i, j))
                elif "target" in element:
                    target = (i, j)
                elif "enemy" in element:
                    enemy.add((i, j))

            if board_row:
                board.append(tuple(board_row))

        board = tuple(board)

        return Level(board, target, enemy), State(player, rocks, water, crosses, keys, player_has_key)
