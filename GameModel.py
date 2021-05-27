from Saper.View.Pole import Pole


class GameModel:

    def __init__(self, new_game_map):
        self.game_map = None
        self.mines = []
        self.flags = []
        self.height = len(new_game_map)
        self.width = len(new_game_map[0])
        self.init_game_map(new_game_map)

    def init_game_map(self, arr):
        self.game_map = [[0 for x in range(self.width)] for y in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                if arr[i][j] == 'b':
                    self.mines.append([i, j])
                self.game_map[i][j] = Pole(i, j, arr[i][j])

    def set_game_controller(self, controller):
        self.controller = controller

    def pole_is_changed(self, height, width):
        if not self.game_map[height][width].viewed:
            if self.game_map[height][width].mine:
                self.controller.game_destroy()
            else:
                self.controller.show_pole(self.game_map[height][width])

    def set_flag(self, x, y):
        if not self.game_map[x][y].viewed and self.game_map[x][y].flag == 0:
            self.flags.append([x, y])
            self.controller.set_flag(x, y)
