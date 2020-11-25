from typing import List, Tuple, Set

# Typing vars.
StaticObject = Tuple[int, int]
StateObject = Set[StaticObject]
StatePlayer = List[int]
LevelBoard = Tuple[Tuple[int]]

class State:
    """
    Clase que guarda el estado de la partida del juego escapa.
    """
    def __init__(
        self,
        player: StatePlayer,
        rocks: StateObject,
        water: StateObject,
        crosses: StateObject,
        key: StaticObject,
        player_has_key: bool,
    ):
        self.player = player
        self.rocks = rocks
        self.water = water
        self.crosses = crosses
        self.key = key
        self.player_has_key = player_has_key

    def get_player(self):
        return self.player

    def get_rocks(self):
        return self.rocks

    def get_water(self):
        return self.water

    def get_crosses(self):
        return self.crosses

    def get_key(self):
        return self.key

    def get_player_has_key(self):
        return self.player_has_key

    def __str__(self):
        return (
              f"\n   * Player: {str(self.player)}"
            + f"\n   * Rocks: {str(self.rocks)}"
            + f"\n   * Water: {str(self.water)}"
            + f"\n   * Crosses: {str(self.crosses)}"
            + f"\n   * Key: {str(self.key)}"
            + f"\n   * Player Has Key: {str(self.player_has_key)}"
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o: "State"):
        return all(
            [
                self.player == o.player,
                self.rocks == o.rocks,
                self.water == o.water,
                self.crosses == o.crosses,
                self.key == o.key,
                self.player_has_key == o.player_has_key,
            ]
        )

    def __hash__(self):
        return hash(
            (
                str(self.player),
                frozenset(self.rocks),
                frozenset(self.water),
                frozenset(self.crosses),
                str(self.key),
                str(self.player_has_key),
            )
        )

class Level:
    """
    Clase del nivel del juego escapa.
    Almacena el tablero, el destino y los enemigos.
    """
    def __init__(self, board: LevelBoard, target: StaticObject, enemies: StaticObject):
        self.board = board
        self.target = target
        self.enemies = enemies

    def get_board(self):
        return self.board

    def get_board_sizes(self):
        return len(self.board), len(self.board[0])

    def get_target(self):
        return self.target

    def get_enemies(self):
        return self.enemies

    def __str__(self):
        return str(self.board) + str(self.target) + frozenset(self.enemies)

    def __repr__(self):
        return str(self.board) + str(self.target) + frozenset(self.enemies)
