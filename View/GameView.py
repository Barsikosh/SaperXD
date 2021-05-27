from tkinter import *
from Saper.View.Pole import Pole


class GameView:

    def __init__(self, controller):
        self.game_map = [[Button] * controller.get_height()] * controller.get_width()
        self.controller = controller
        self.game_window = None

    def update_map(self, new_map):
        self.game_map = new_map

    def set_flag(self, x, y):
        self.game_map[x][y].configure(text="F", bg='green')

    def show_clear_pole(self, pole):
        if not pole.viewed:
            if pole.mine:
                return True
            else:
                pole.flag = 1
                self.game_map[pole.row][pole.column].configure(text=pole.value, bg='white')
                pole.viewed = True
                return False

    def destroy_all(self):
        lose_window = Tk()
        lose_window.geometry('400x250')
        lbl = Label(lose_window, text="YOU DEAD", font=("Arial Bold", 30), bg='red')
        lbl.grid(row=200, column=150)
        self.game_window.destroy()

    def create_field(self):
        self.game_window = Tk()
        self.game_window.title("Сапёр")
        buttons = []
        for i in range(len(self.game_map)):
            temp = []
            for j in range(len(self.game_map[0])):
                button = Button(width=3)
                button.bind('<Button-1>', lambda event, x=i, y=j: self.controller.pole_click_action(event, x, y))
                button.bind('<Button-3>', lambda event, x=i, y=j: self.controller.flag_added(event, x, y))
                button.grid(row=i, column=j)
                temp.append(button)
            buttons.append(temp)
        self.game_map = buttons
        self.game_window.mainloop()
