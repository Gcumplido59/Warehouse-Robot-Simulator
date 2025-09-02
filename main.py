from warehouse import Almacen
from robot import Robot
from obstacle import Obstacle
from package import Package

# Create the world and its objects
mi_almacen = Almacen(10, 5)
mi_robot = Robot(fila=2, columna=1)
mi_paquete = Package(fila=4, columna=8)
obstaculos = [
    Obstacle(fila=1, columna=3),
    Obstacle(fila=2, columna=3),
    Obstacle(fila=3, columna=3),
    Obstacle(fila=3, columna=4),
    Obstacle(fila=3, columna=5)
]

# Add everything to the warehouse
mi_almacen.add_robot(mi_robot)
mi_almacen.place_object(mi_paquete, '2')
for obs in obstaculos:
    mi_almacen.place_object(obs, '1')

# Show the initial state of the simulation
print("Simulation Start:")
mi_almacen.display()