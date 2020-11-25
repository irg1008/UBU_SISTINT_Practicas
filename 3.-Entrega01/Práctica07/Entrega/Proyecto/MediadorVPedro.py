from DynamicCodeLoader import loadDynamicCode
from Loader import Loader
import time

"""
Clase Mediador

Implementa el patrón de diseño singleton

Interrelaciona las clases de interfaz entre si y con el modelo 
para que estas clases no tengan acoplamiento entre si.

"""


class Mediator(object):
    INSTANCE = None

    def __init__(self, modelPath, aStarPath, nodesPath):
        """ Constructor por defecto

        Devuelve un objeto de tipo mediador

        Parámetros:
        Ninguno.
        """
        self.sol = []
        if self.INSTANCE:
            raise ValueError("An instantiation already exists!")
        # inicialización

        self.model = None
        self.search = None
        self.nodes = None
        self.manual = True

        if modelPath:
            self.model = loadDynamicCode(modelPath, "Model")
            print(self.model)

        if aStarPath:
            self.search = loadDynamicCode(aStarPath, "Search")
            self.manual = False

        if nodesPath:
            self.nodes = loadDynamicCode(nodesPath, "Nodes")
            self.manual = False

    @classmethod
    def get_instance(cls, modelPath=None, aStarPath=None, nodesPath=None):
        if cls.INSTANCE is None:
            cls.INSTANCE = Mediator(modelPath, aStarPath, nodesPath)
        return cls.INSTANCE

    def register_ui(self, ui):
        self.ui = ui

        dropdown, self.visor, control = ui.get_ui_elements().children

        directions, actions = control.children

        box1, box2 = directions.children
        _, up = box1.children
        left, down, right = box2.children

        action_buttons = actions.children

        l = Loader()
        levels = l.get_all_levels()

        dropdown.options = levels

        dropdown.observe(
            lambda name: self.update_level_observer(name), names="value")

        self.filename = levels[0]
        self.update_level_from_file(self.filename)

        up.on_click(lambda button: self.button_action_event(button))
        down.on_click(lambda button: self.button_action_event(button))
        right.on_click(lambda button: self.button_action_event(button))
        left.on_click(lambda button: self.button_action_event(button))

        for abutton in action_buttons:
            abutton.on_click(lambda button: self.button_action_event(button))

    def update_level_observer(self, name):
        self.filename = name['new']
        self.update_level_from_file(self.filename)

    def update_level_from_file(self, filename):
        l = Loader()
        level_txt = l.get_txt_level(filename)
        self.level, self.state = l.load_level(level_txt)
        htmlStr = self.ui.get_html(self.level, self.state)
        self.visor.value = htmlStr

    def update_game(self, desc):
        #actualiza_turno = False
        mov = []
        if desc == "^":
            mov = [-1, 0]
        elif desc == "v":
            mov = [1, 0]
        elif desc == ">":
            mov = [0, 1]
        elif desc == "<":
            mov = [0, -1]

        if mov:
            self.state = self.model.move(self.level, self.state, mov)

        else:
            # reinicio
            self.update_level_from_file(self.filename)
            self.solucion = []
            self.id_sol = 0

    def button_action_event(self, button):
        desc = button.description
        if desc in ["^", "v", "<", ">", "Change", "Reset"]:
            # Actualiza Juego
            self.update_game(desc)

        elif desc == "Resolve" and self.search and self.nodes:
            initialNode = self.nodes.initial_node_JE(
                self.level, self.state, self.nodes.heuristic_JE)

            # Añadido por Estudiante.
            # -----------------------------
            self.show_executing()
            # Fin Añadido por Estudiante.
            # -----------------------------

            self.sol = self.search.AStar(
                initialNode, self.nodes.successors_JE, self.nodes.goal_JE, self.nodes.heuristic_JE)

            self.iterations = self.nodes.iterations
            self.total_cost = self.nodes.total_cost

            # Bloque por Estudiante.
            # -----------------------------
            self.elapsed_time = self.nodes.elapsed_time
            self.show_gui()
            time.sleep(0.5)  # Wait .5 second to show animation.
            
            # Animate every .25s.
            for s in self.sol:
                time.sleep(0.25)
                self.state = s
                self.show_gui()
            # -----------------------------
            # Fin Añadido por Estudiante.

            self.id_sol = 0
            # print("self.sol")
            # print(self.sol)

        elif desc == "Next":
            if len(self.sol) > 0 and len(self.sol) > self.id_sol+1:
                self.id_sol += 1
                s = self.sol[self.id_sol]
                self.state = s

        elif desc == "Previous":
            if len(self.sol) > 0 and self.id_sol > 0:
                self.id_sol -= 1
                s = self.sol[self.id_sol]
                self.state = s

        self.show_gui()

    def show_gui(self):
        htmlStr = self.ui.get_html(self.level, self.state)

        if not self.manual and len(self.sol) > 0:
            htmlStr += "<br/> Nodos evaluados <br/>"
            htmlStr += str(self.iterations)
            htmlStr += "<br/> Coste de la solucion <br/>"
            htmlStr += str(self.total_cost)
            htmlStr += "<br/> Tiempo empleado <br/>"
            htmlStr += f"{str(self.elapsed_time)} segundos"
            htmlStr += "<br/> ______________ <br/>"

        self.visor.value = htmlStr

        if self.model.is_goal(self.state):
            self.visor.value += "¡GANASTE! <br> Si hubiera otro nivel, ¡cárgalo!"

    # Añadido por Estudiante.
    # -----------------------------
    def show_executing(self):
        htmlStr = self.ui.get_html(self.level, self.state)
        htmlStr += "Resolviendo algoritmo, solo serán unos segundos"
        htmlStr += "<br/> ______________ <br/>"
        self.visor.value = htmlStr
    # -----------------------------
    # Fin Añadido por Estudiante.
