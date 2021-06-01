# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Controller.Controller import Controller
from View.GameView import GameView



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
if __name__ == '__main__':
    controller = Controller()
    f = GameView(controller)
    controller.set_game_view(f)
    f.init_view()
