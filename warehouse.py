# In warehouse.py

class Almacen:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.robot = None  # We'll store the robot here
        self.cuadricula = [['0' for _ in range(ancho)] for _ in range(alto)]

    def add_robot(self, robot_obj):
        self.robot = robot_obj
        # Place the robot for the first time
        fila, col = self.robot.fila, self.robot.columna
        self.cuadricula[fila][col] = 'R'

    def move_robot(self, direction):
        if not self.robot:
            print("No robot in the warehouse!")
            return

        # 1. Erase old position
        old_fila, old_col = self.robot.fila, self.robot.columna
        self.cuadricula[old_fila][old_col] = '0'

        # 2. Call the robot's own move method
        if direction == "up":
            self.robot.move_up()
        elif direction == "down":
            self.robot.move_down()
        elif direction == "left":
            self.robot.move_left()
        elif direction == "right":
            self.robot.move_right()

        # 3. Draw new position
        new_fila, new_col = self.robot.fila, self.robot.columna
        self.cuadricula[new_fila][new_col] = 'R'

    def display(self):
        # (display method remains the same)
        print("--- Almacén ---")
        for fila in self.cuadricula:
            print(' '.join(fila))
        print("---------------")