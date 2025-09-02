# In main.py
from warehouse import Almacen
from robot import Robot
from obstacle import Obstacle # Import the new Obstacle class

# Setup
mi_almacen = Almacen(10, 5)
mi_robot = Robot(fila=2, columna=1)

# Create some obstacles
obstaculo_1 = Obstacle(fila=2, columna=2)
obstaculo_2 = Obstacle(fila=1, columna=1)

# Add everything to the warehouse
mi_almacen.add_robot(mi_robot)
mi_almacen.place_object(obstaculo_1, '🧱')
mi_almacen.place_object(obstaculo_2, '🧱')

# Show initial state
print("Initial State:")
mi_almacen.display()

# --- Test the collision ---
# Try to move right into the obstacle
print("\nAttempting to move RIGHT...")
mi_almacen.move_robot("right")

# Try to move up into the other obstacle
print("\nAttempting to move UP...")
mi_almacen.move_robot("up")

print("\nFinal State:")
mi_almacen.display()