import tkinter
from datetime import time
from tkinter import *
import threading
from Saper2.Model.GameModel import GameModel
from Saper2.Model.MapGenerator import Creating_Map
import time

class GameView(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.lvl = None
        self.lbl_hard = None
        self.lvl1 = None
        self.lvl2 = None
        self.lvl3 = None
        self.btn_start = None
        self.lbl_timer = None
        self.btn_break = None
        self.play = False
        self.time_pass = 0


    def init_view(self):

        self.stage_start()
        self.mainloop()


    def create_start_menu(self):
        self.clear()
        self.title("Сапёр")
        self.geometry('450x250')


        self.lbl_hard = Label(self, text="HARD-LVL")
        self.lbl_hard.grid(column=0, row=0)

        self.lvl = IntVar()
        self.lvl1 = Radiobutton(self, text='Первый', value=0, variable=self.lvl)
        self.lvl2 = Radiobutton(self, text='Второй', value=1, variable=self.lvl)
        self.lvl3 = Radiobutton(self, text='Третий', value=2, variable=self.lvl)
        self.lvl1.grid(column=0, row=1)
        self.lvl2.grid(column=0, row=2)
        self.lvl3.grid(column=0, row=3)

        self.btn_start = Button(self, width=10, text="START", background='green')
        self.btn_start.bind('<Button-1>', lambda event: self.controller.start_game(event))
        self.btn_start.grid(column=0, row=4)

        self.lbl_timer = Label(self, text="00:00", background='green')
        self.lbl_timer.grid(column=0, row=0)

        self.btn_break = Button(self, width=10, text="BREAK", background='yellow')
        self.btn_break.bind('<Button-1>', lambda event: self.controller.stop_game(event))
        self.btn_break.grid(column=0, row=1)
        self.btn_break.grid_remove()
        self.lbl_timer.grid_remove()

    def update_map(self, new_map):
        self.game_map = new_map

    def set_size(self, size):
        self.geometry(size)

    def set_flag(self, x, y):
        self.game_map[x][y].configure(text="F", bg='green')

    def create_pole(self, x, y):
        button = Button(width=3)
        button.bind('<Button-1>', lambda event, nx=x, ny=y: self.controller.pole_click_action(event, nx, ny))
        button.bind('<Button-3>', lambda event, nx=x, ny=y: self.controller.flag_added(event, nx, ny))
        button.grid(row=x, column=y + 1)
        return button

    def unset_flag(self, x, y):
        self.game_map[x][y] = self.create_pole(x, y)

    def show_clear_pole(self, x, y, value):
        self.game_map[x][y].configure(text=value, bg='white')

    def update_timer(self, time):
        if self.play:
            self.lbl_timer = Label(self.game_window, text=time, background='green')

    def create_field(self):
        self.game_map = [[Button] * self.controller.get_height()] * self.controller.get_width()
        buttons = []
        for i in range(len(self.game_map)):
            temp = []
            for j in range(len(self.game_map[0])):
                button = self.create_pole(i, j)
                temp.append(button)
            buttons.append(temp)
        self.game_map = buttons


    def clear(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()

    def destroy_all(self):
        self.clear()
        self.geometry('450x250')
        lbl = Label(self, text=f"YOU DEAD FOR {self.time_pass}", font=("Arial Bold", 30), bg='red')
        lbl.grid(row=200, column=150)
        restart_button = Button(width=20, text="RESTART")
        restart_button.grid(row=250, column=150)
        restart_button.bind('<Button-1>', lambda event: self.create_start_menu())

    def game_won(self):
        self.clear()
        self.geometry('450x250')
        lbl = Label(self, text=f"YOU WIN FOR {self.time_pass}", font=("Arial Bold", 30), bg='green')
        lbl.grid(row=200, column=150)
        restart_button = Button(self.game_window, width=20, text="RESTART")
        restart_button.grid(row=250, column=150)
        restart_button.bind('<Button-1>', lambda event: self.create_start_menu())

    def stage_start(self):
        self.set_size('400x250')
        self.create_start_menu()

    def watch_timer(self):
        self.btn_break.grid()
        self.lbl_timer.grid()
        while True:
            self.time_pass = self.controller.get_time()
            self.lbl_timer.config(text=self.controller.get_time())

    def stage_play(self):
        self.play = True
        self.clear()

        gameMap = Creating_Map(self.lvl.get())
        if self.lvl.get() == 1:
            self.set_size('700x450')
        elif self.lvl.get() == 2:
            self.set_size('1100x800')

        gameModel = GameModel(gameMap)
        self.controller.set_game_model(gameModel)
        gameModel.set_game_controller(self.controller)
        threading.Thread(target=self.controller.start_timer, daemon=True).start()
        threading.Thread(target=self.create_field).start()
        threading.Thread(target=self.watch_timer, args=(), daemon=True).start()