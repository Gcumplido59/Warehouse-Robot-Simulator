# In main.py
from warehouse import Almacen
from robot import Robot

# Setup
mi_almacen = Almacen(10, 5)
mi_robot = Robot(fila=3, columna=4) # Start at a different position
mi_almacen.add_robot(mi_robot)

# Show initial state
print("Initial Position:")
mi_almacen.display()

# Move the robot and show the new state
print("\nMoving UP...\n")
mi_almacen.move_robot("up")

print("New Position:")
mi_almacen.display()