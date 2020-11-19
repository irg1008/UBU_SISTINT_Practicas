from ipywidgets import HTML, Dropdown, Button, HBox, VBox


class Gui:
    def __init__(self, manual=True):
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
        # change = Button(description="Change")
        empty = Button(description=" ")
        empty.margin = 2
        directions = VBox([HBox([empty, up]), HBox([left, down, right])])

        actions = self.get_actions()
        control = VBox([directions, actions])

        self.ui = VBox(children=[dropdown, viewfinder, control])

    def get_content(self, level, state, coord):
        coord = tuple(coord)
        content = [None, None]

        board = level.get_board()
        target = level.get_target()
        enemy = level.get_enemy()
        rocks = state.get_rocks()
        water = state.get_water()
        keys = state.get_keys()
        crosses = state.get_crosses()
        player = state.get_player()

        def is_floor(board, coord):
            try:
                x, y = coord
                return board[x][y] == 1
            except IndexError:
                return False

        # Floor/Wall/Target.
        if coord == target:
            content[0] = ("target")
        elif is_floor(board, coord):
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
        elif coord in keys:
            content[1] = ("key")

        # Character.
        if list(coord) == player:
            content[1] = ("player")
        elif coord == enemy:
            content[1] = ("enemy")

        return content

    def get_ui_elements(self):
        return self.ui

    def get_actions(self):
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

    def get_html(self, level, state):
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
