from warehouse import Warehouse
from robot import Robot
from visualizer import Visualizer

def main():
    """Initializes and runs the Warehouse Robot Simulator application.

    This function serves as the main entry point for the program. It sets up
    the core components:
    1. A `Warehouse` instance representing the grid environment.
    2. A `Robot` instance placed at a fixed starting position.
    3. A `Visualizer` instance which takes the warehouse and handles the
       Pygame loop for rendering and user interaction.
    """
    # Create an empty warehouse
    my_warehouse = Warehouse(10, 8)
    
    # Create the robot at a fixed starting position (0, 0)
    my_robot = Robot(row=0, column=0)
    my_warehouse.add_robot(my_robot)

    # The visualizer handles the main application loop
    app = Visualizer(warehouse=my_warehouse)
    app.run()

if __name__ == '__main__':
    main()