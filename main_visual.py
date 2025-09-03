# In main_visual.py
from warehouse import Almacen
from robot import Robot
from obstacle import Obstacle
from package import Package
from visualizer import Visualizer

def main():
    # --- SETUP (Same as before) ---
    mi_almacen = Almacen(10, 5)
    mi_robot = Robot(fila= 0, columna=1)
    mi_paquete = Package(fila=2, columna=1)
    obstaculos = [
        Obstacle(fila=1, columna=3), Obstacle(fila=2, columna=3),
        Obstacle(fila=3, columna=3), Obstacle(fila=3, columna=4),
        Obstacle(fila=3, columna=5), Obstacle(fila=1, columna=0),
        Obstacle(fila=1, columna=1), Obstacle(fila=1, columna=2),
        Obstacle(fila=3, columna=6), Obstacle(fila=3, columna=7)
    ]

    mi_almacen.add_robot(mi_robot)
    mi_almacen.add_package(mi_paquete)
    for obs in obstaculos:
        mi_almacen.place_object(obs, '🧱')

    # --- LOGIC (Same as before) ---
    print("Searching for a path...")
    path = mi_almacen.find_path()

    if path:
        print("Path Found! Launching visualizer...")
        # --- VISUALIZATION ---
        app = Visualizer(almacen=mi_almacen, path=path)
        app.run()
    else:
        print("No path could be found.")

if __name__ == '__main__':
    main()