class State:
    def __init__(self, player, rocks, water, crosses, keys):
        self.player = player
        self.rocks = rocks
        self.water = water
        self.crosses = crosses
        self.keys = keys

    def get_player(self):
        return self.player

    def get_rocks(self):
        return self.rocks

    def get_water(self):
        return self.water

    def get_crosses(self):
        return self.crosses

    def get_keys(self):
        return self.keys

    def __str__(self):
        return (str(self.player) +
                str(self.rocks) +
                str(self.water) +
                str(self.crosses) +
                str(self.keys))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        return all([self.rocks == o.rocks,
                    self.water == o.water,
                    self.crosses == o.crosses,
                    self.keys == o.keys])

    def __hash__(self):
        return hash(str(self.player),
                    frozenset(self.rocks),
                    frozenset(self.water),
                    frozenset(self.crosses),
                    frozenset(self.keys))


class Level:
    def __init__(self, board, target, enemy):
        self.board = board
        self.target = target
        self.enemy = enemy

    def get_board(self):
        return self.board

    def get_board_sizes(self):
        return len(self.board), len(self.board[0])

    def get_target(self):
        return self.target

    def get_enemy(self):
        return self.enemy

    def __str__(self):
        return (str(self.board) +
                str(self.target) +
                str(self.enemy))

    def __repr__(self):
        return (str(self.board) +
                str(self.target) +
                str(self.enemy))
