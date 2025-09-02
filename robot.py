# In robot.py

class Robot:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def move_up(self):
        self.fila -= 1

    def move_down(self):
        self.fila += 1

    def move_left(self):
        self.columna -= 1

    def move_right(self):
        self.columna += 1