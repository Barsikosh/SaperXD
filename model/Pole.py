from tkinter import Button, Label


class Pole:

    def __init__(self, row, column, element):
        self.mine = False
        self.value = 'b'
        self.flag = 0
        self._check_bomb(element)
        self.viewed = False
        self.row = row
        self.column = column

    def _check_bomb(self, element):
        if element == 'b':
            self.mine = True
        elif element == 0:
            self.value = ""
        else:
            self.value = element
