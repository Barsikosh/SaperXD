import celery
import threading
import time


class Controller:
    def __init__(self):
        self.game_model = None

    def set_game_model(self, game_model):
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

    def show_pole(self, x, y, value):
        self.game_view.show_clear_pole(x, y, value)

    def flag_added(self, event, x, y):
        self.game_model.set_flag(x, y)

    def set_flag(self, x, y):
        self.game_view.set_flag(x, y)

    def set_game_view(self, game_view):
        self.game_view = game_view

    def start_game(self, event):
        self.game_view.stage_play()

    def start_timer(self):
        self.game_model.start_timer()

    def get_time(self):
        return self.game_model.get_left_time()

    def stop_game(self, event):
        self.game_view.stage_start()

    def unset_flag(self, x, y):
        self.game_view.unset_flag(x, y)

    def game_won(self):
        self.game_view.game_won()

    def get_method_timer(self):
        return self.timer_feed_back

    def set_method_timer(self, method):
        self.timer_feed_back = method
