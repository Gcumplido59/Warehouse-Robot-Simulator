from warehouse import Almacen
from robot import Robot
from visualizer import Visualizer

def main():
    # Create an empty warehouse
    mi_almacen = Almacen(10, 8)
    
    # Create the robot at a fixed starting position (0, 0)
    mi_robot = Robot(fila=0, columna=0)
    mi_almacen.add_robot(mi_robot)

    # The visualizer now handles all the logic
    app = Visualizer(almacen=mi_almacen)
    app.run()

if __name__ == '__main__':
    main()