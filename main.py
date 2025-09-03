# In main.py
from warehouse import Almacen
from robot import Robot
from obstacle import Obstacle
from package import Package

# --- SETUP ---
mi_almacen = Almacen(10, 5)
mi_robot = Robot(fila=2, columna=1)
mi_paquete = Package(fila=4, columna=8)
obstaculos = [
    Obstacle(fila=1, columna=3), Obstacle(fila=2, columna=3),
    Obstacle(fila=3, columna=3), Obstacle(fila=3, columna=4),
    Obstacle(fila=3, columna=5)
]

mi_almacen.add_robot(mi_robot)
mi_almacen.add_package(mi_paquete)
for obs in obstaculos:
    mi_almacen.place_object(obs, '1')

print("Initial State of the Simulation:")
mi_almacen.display()

# --- FIND AND DISPLAY THE PATH ---
print("\nSearching for a path...")
path = mi_almacen.find_path()

if path:
    print("Path Found!")
    mi_almacen.display_path(path)
else:
    print("No path could be found.")