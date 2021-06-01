from tkinter import Button, Label


class Pole:

    def __init__(self, row, column, element):
        self.mine = False
        self.value = 'b'
        self.flag = 0
        self._check_bomb(element)
        # self.button = Button(master, width=3,
        #  command=lambda pole=self: click_event(pole))  # Создаем для нашего поля атрибут 'button'
        # self.button.grid(row=row, column=column)
        self.viewed = False  # Открыто/закрыто поле
        # self.around = []  # Массив, содержащий координаты соседних клеток
        self.row = row  # Строка
        self.column = column  # Столбец

    def _check_bomb(self, element):
        if element == 'b':
            self.mine = True
        elif element == 0:
            self.value = ""
        else:
            self.value = element

    def view(self):
        if not self.viewed:
            if self.mine:
                return True
            else:
                self.flag = 1
                self.button.configure(text='1', bg='white')
                self.viewed = True
                return False
