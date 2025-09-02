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

    def place_object(self, obj, simbolo):
        fila, col = obj.fila, obj.columna
        self.cuadricula[fila][col] = simbolo


    def move_robot(self, direction):
        if not self.robot:
            print("No robot in the warehouse!")
            return

        # Calculate potential next position
        next_fila, next_col = self.robot.fila, self.robot.columna
        if direction == "up":
            next_fila -= 1
        elif direction == "down":
            next_fila += 1
        elif direction == "left":
            next_col -= 1
        elif direction == "right":
            next_col += 1

        # --- NEW OBSTACLE CHECK ---
        # Check 1: Is the move within the grid boundaries?
        if not (0 <= next_fila < self.alto and 0 <= next_col < self.ancho):
            print(f"Move '{direction}' is out of bounds.")
            return

        # Check 2: Is the destination cell empty?
        if self.cuadricula[next_fila][next_col] != '_':
            print(f"Move '{direction}' is blocked by an object!")
            return
        
        # If all checks pass, then move the robot
        # Erase old position
        self.cuadricula[self.robot.fila][self.robot.columna] = '_'
        
        # Update robot's internal position
        self.robot.fila = next_fila
        self.robot.columna = next_col
        
        # Draw new position
        self.cuadricula[self.robot.fila][self.robot.columna] = 'R'

    def display(self):
        # (display method remains the same)
        print("--- Almacén ---")
        for fila in self.cuadricula:
            print(' '.join(fila))
        print("---------------")