import celery
import threading

class Controller:
    def __init__(self, game_model):
        self.game_model = game_model


    def pole_click_action(self, event, x, y):
        self.game_model.pole_is_changed(x, y)


    def game_destroy(self):
        self.game_view.destroy_all()

    def get_width(self):
        return self.game_model.width


    def get_height(self):
        return self.game_model.height

    def get_game_map(self):
        return self.game_model.game_map


    def show_pole(self, pole):
        self.game_view.show_clear_pole(pole)

    def flag_added(self, event, x, y):
        self.game_model.set_flag(x, y)

    def set_flag(self, x, y):
        self.game_view.set_flag(x, y)

    def set_game_view(self, game_view):
        self.game_view = game_view
