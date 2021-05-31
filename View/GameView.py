import tkinter
from datetime import time
from tkinter import *
import threading
import time

from Saper2.Model.GameModel import GameModel
from Saper2.Model.MapGenerator import Creating_Map


class GameView(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.controller.set_method_timer(self.update_timer)
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
        self["bg"] = "#bcb9ed"
        self.geometry('250x330')

        self.lbl_hard = Label(self, text="  Выберите уровень:\n💣💣💣\n", font="Calibri 19 bold", bg="#bcb9ed")
        self.lbl_hard.grid(column=2, row=0)

        self.lvl = IntVar()
        self.lvl1 = Radiobutton(self, text="Лёгкий 😊", font="Calibri 22 bold", bg="#54e89b", value=0,
                                variable=self.lvl)
        self.lvl2 = Radiobutton(self, text="Средний 😐", font="Calibri 22 bold", bg="#ed9747", value=1,
                                variable=self.lvl)
        self.lvl3 = Radiobutton(self, text="Сложный 😞", font="Calibri 22 bold", bg="#ed3939", value=2,
                                variable=self.lvl)
        self.lvl1.grid(column=2, row=1, ipadx=14)
        self.lvl2.grid(column=2, row=2, ipadx=4)
        self.lvl3.grid(column=2, row=3)
        self.temp = Label(self, text="", bg="#bcb9ed")
        self.temp.grid(column=0, row=4)
        self.btn_start = Button(self, text="💣 START 💣", font="Calibri 16 bold", bg='white')
        self.btn_start.bind('<Button-1>', lambda event: self.controller.start_game(event))
        self.btn_start.grid(column=2, row=5)

        self.lbl_timer = Label(self, text="00:00", font="Calibri 12 bold", bg='#f52c2c')
        self.lbl_timer.grid(column=0, row=0)

        self.btn_break = Button(self, width=10, text="BREAK", bg='yellow')
        self.btn_break.bind('<Button-1>', lambda event: self.controller.stop_game(event))
        self.btn_break.grid(column=0, row=1)
        self.btn_break.grid_remove()
        self.lbl_timer.grid_remove()

    def update_map(self, new_map):
        self.game_map = new_map

    def set_size(self, size):
        self.geometry(size)

    def set_flag(self, x, y):
        self.game_map[x][y].configure(text="🚩", bg='#7ef291')

    def create_pole(self, x, y):
        button = Button(width=3, bg="#a9a9a9")
        button.bind('<Button-1>', lambda event, nx=x, ny=y: self.controller.pole_click_action(event, nx, ny))
        button.bind('<Button-3>', lambda event, nx=x, ny=y: self.controller.flag_added(event, nx, ny))
        button.grid(row=x, column=y + 1, sticky='NSEW')
        return button

    def unset_flag(self, x, y):
        self.game_map[x][y] = self.create_pole(x, y)

    def show_clear_pole(self, x, y, value):
        self.game_map[x][y].configure(text=value, bg='white')

    def create_field(self):
        self.game_map = [[Button] * self.controller.get_height()] * self.controller.get_width()
        buttons = []
        for i in range(len(self.game_map)):
            temp = []
            for j in range(len(self.game_map[0])):
                button = self.create_pole(i, j)
                temp.append(button)
            buttons.append(temp)
        for k in range(len(self.game_map)):
            for l in range(len(self.game_map[0])):
                self.grid_columnconfigure(l + 1, weight=1)
            self.grid_rowconfigure(k, weight=1)
        self.game_map = buttons

    def clear(self):
        list = self.grid_slaves()
        for l in list:
            l.destroy()

    def destroy_all(self):
        self.clear()
        self.geometry('324x250')
        lbl = Label(self, text=f"YOU DEAD FOR {self.time_pass}", font="Calibri 27 bold", bg='red')
        lbl.grid(row=0, column=0)
        lbl2 = Label(self, text="😈💣😈💣😈💣\n", font="Calibri 22 bold", fg="black", bg="#bcb9ed")
        lbl2.grid(row=1, column=0)
        restart_button = Button(width=20, text="༼ つ ◕_◕ ༽つ RESTART", height=3, font="Calibri 16 bold")
        restart_button.grid(row=2, column=0)
        restart_button.bind('<Button-1>', lambda event: self.create_start_menu())

    def game_won(self):
        self.clear()
        self.geometry('324x250')
        lbl = Label(self, text=f"YOU WIN FOR {self.time_pass}", font="Calibri 27 bold", bg='green')
        lbl.grid(row=0, column=0)
        lbl2 = Label(self, text="👍✨💯👌\n", font="Calibri 22 bold", bg='#bcb9ed', fg="yellow")
        lbl2.grid(row=1, column=0)
        restart_button = Button(self.game_window, width=18, text="👉 RESTART 👈", height=3, font="Calibri 16 bold")
        restart_button.grid(row=2, column=0)
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

    def update_timer(self):
        if self.play:
            self.time_pass = self.controller.get_time()
        self.lbl_timer.config(text=self.time_pass)

    def stage_play(self):
        self.play = True
        self.clear()
        gameMap = Creating_Map(self.lvl.get())

        if self.lvl.get() == 0:
            self.set_size('350x230')
        elif self.lvl.get() == 1:
            self.set_size('600x450')
        elif self.lvl.get() == 2:
            self.set_size('1000x700')

        gameModel = GameModel(gameMap)
        self.controller.set_game_model(gameModel)
        gameModel.set_game_controller(self.controller)
        threading.Thread(target=self.controller.start_timer, daemon=True).start()
        threading.Thread(target=self.create_field).start()
        self.btn_break.grid()
        self.lbl_timer.grid()
