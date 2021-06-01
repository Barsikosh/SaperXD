from Saper2.Model.Pole import Pole
from Saper2.Model.Timer import Timer


class GameModel:

    def __init__(self, new_game_map):
        self.count_mines = 0
        self.game_map = None
        self.flags = []
        self.height = len(new_game_map)
        self.width = len(new_game_map[0])
        self.init_game_map(new_game_map)
        self.controller = None
        self.opened_fields = 0
        self.timer = None

    def init_game_map(self, arr):
        self.game_map = [[-999 for _ in range(self.width)] for y in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.game_map[i][j] = Pole(i, j, arr[i][j])
                if self.game_map[i][j].mine:
                    self.count_mines+=1

    def start_timer(self):
        self.timer = Timer()
        self.timer.set_feed_back(self.controller.get_method_timer())
        self.timer.start()

    def get_left_time(self):
        return self.timer.time()

    def game_lose(self):
        self.controller.game_destroy()


    def set_game_controller(self, controller):
        self.controller = controller


    def pole_is_changed(self, height, width):
        if not self.game_map[height][width].viewed:
            if self.game_map[height][width].mine:
                self.game_lose()
            else:
                self.open_cell(height, width)

    def open_cell(self, x, y):
        if (x < 0) or (y < 0) or (x >= self.height) or (y >= self.width):
            return
        if self.game_map[x][y].viewed:
            return
        pole = self.game_map[x][y]
        pole.viewed = True
        pole.flag = 1
        self.opened_fields += 1
        self.controller.show_pole(x, y, pole.value)
        if self.opened_fields >= self.width * self.height - self.count_mines:
            self.controller.game_won()
        self.open_neighbor(x, y)

    def check_bombs(self, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not ((x + dx < 0) or (y + dy < 0) or (x + dx >= self.height) or (y + dy >= self.width)):
                    if self.game_map[x + dx][y + dy].mine:
                        return True
        return False

    def open_neighbor(self, x, y):
        if self.check_bombs(x, y):
            return
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx == 0) and (dy == 0):
                    continue
                self.open_cell(x + dx, y + dy)


    def set_flag(self, x, y):
        if not self.game_map[x][y].viewed:
            if self.game_map[x][y].flag == 0:
                self.game_map[x][y].flag = 1
                self.flags.append([x, y])
                self.controller.set_flag(x, y)
            else:
                self.game_map[x][y].flag = 0
                self.controller.unset_flag(x, y)
