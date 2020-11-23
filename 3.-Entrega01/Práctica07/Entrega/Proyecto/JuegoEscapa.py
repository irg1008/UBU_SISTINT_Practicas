class State:
    def __init__(self, player, rocks, water, crosses, keys, player_has_key):
        self.player = player
        self.rocks = rocks
        self.water = water
        self.crosses = crosses
        self.keys = keys
        self.player_has_key = player_has_key

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

    def get_player_has_key(self):
        return self.player_has_key

    def __str__(self):
        return (f"\n-> Player: {str(self.player)}" +
                f"\n-> Rocks: {str(self.rocks)}" +
                f"\n-> Water: {str(self.water)}" +
                f"\n-> Crosses: {str(self.crosses)}" +
                f"\n-> Keys: {str(self.keys)}" +
                f"\n-> Player Has Key: {str(self.player_has_key)}")

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        return all([self.player == o.player,
                    self.rocks == o.rocks,
                    self.water == o.water,
                    self.crosses == o.crosses,
                    self.keys == o.keys,
                    self.player_has_key == o.player_has_key])

    def __hash__(self):
        return hash((str(self.player),
                     frozenset(self.rocks),
                     frozenset(self.water),
                     frozenset(self.crosses),
                     frozenset(self.keys),
                     str(self.player_has_key)))


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

