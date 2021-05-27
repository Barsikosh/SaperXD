from Saper.Controller import Controller
from Saper.GameModel import GameModel
from Saper.MapGenerator import Creating_Map
from Saper.View.GameView import GameView

gameMap = Creating_Map(0)
gameModel = GameModel(gameMap)
controller = Controller(gameModel)
gameModel.set_game_controller(controller)
f = GameView(controller)
controller.set_game_view(f)
f.create_field()
