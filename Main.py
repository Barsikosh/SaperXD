from Saper2.Controller.Controller import Controller
from View.GameView import GameView

controller = Controller()
f = GameView(controller)
controller.set_game_view(f)
f.init_view()
