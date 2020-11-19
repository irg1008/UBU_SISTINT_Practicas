from os import listdir
from os.path import join, isfile

from pathlib import Path

def get_all_levels():
    abs_path = Path(__file__).parent
    levels_path = join(abs_path, "levels")

    def checks_conditions(file: str):
        return (
            file.endswith(".txt") and
            file.startswith("level") and
            isfile(join(levels_path, file)))

    files = [
        join(levels_path, file)
        for file in listdir(levels_path)
        if checks_conditions(file)]

    return files


def get_map_code(char: str):
    code_char_dictionary = {
        "-": 1,
        "¡": 2,
        "*": 3,
        "!": 4,
        "+": 5,
        "@": 6
    }

    code = code_char_dictionary.get(char)

    return code or 0


def get_game(filename: str):
    file = open(filename, "r", encoding="utf-8")
    lines = file.readlines()

    game_map = [[get_map_code(char)
                 for char in line if char != "\n"] for line in lines]

    return game_map
