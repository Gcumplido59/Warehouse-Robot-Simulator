from collections import deque

class Almacen:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.robot = None
        self.package = None # Keep track of the package
        self.cuadricula = [['0' for _ in range(ancho)] for _ in range(alto)]

    def add_robot(self, robot_obj):
        self.robot = robot_obj
        self.cuadricula[self.robot.fila][self.robot.columna] = 'R'

    def add_package(self, package_obj):
        self.package = package_obj
        self.cuadricula[self.package.fila][self.package.columna] = '📦'

    def place_object(self, obj, simbolo):
        self.cuadricula[obj.fila][obj.columna] = simbolo

    def find_path(self):
        if not self.robot or not self.package:
            print("Robot or package not in warehouse.")
            return None

        start_pos = (self.robot.fila, self.robot.columna)
        goal_pos = (self.package.fila, self.package.columna)

        # 1. Initialize the queue and visited set
        queue = deque([[start_pos]]) # The queue stores entire paths
        visited = {start_pos}

        # 2. Start the search loop
        while queue:
            # 3. Get the oldest path from the queue
            current_path = queue.popleft()
            current_pos = current_path[-1]

            # 4. Check for success
            if current_pos == goal_pos:
                return current_path # Path found!

            # 5. Explore neighbors
            # Moves: Up, Down, Left, Right
            for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
                n_fila, n_col = neighbor_pos

                # 6. Check if the neighbor is valid
                if (0 <= n_fila < self.alto and
                    0 <= n_col < self.ancho and
                    self.cuadricula[n_fila][n_col] in ['0', '📦'] and
                    neighbor_pos not in visited):
                    
                    # 7. Add neighbor to the queue and visited set
                    visited.add(neighbor_pos)
                    new_path = list(current_path)
                    new_path.append(neighbor_pos)
                    queue.append(new_path)
    # Add this method inside the Almacen class
    def display_path(self, path):
        # Draw the path on the grid
        for pos in path:
            fila, col = pos
            if self.cuadricula[fila][col] == '0':
                self.cuadricula[fila][col] = '.'
        self.display()
        # 8. If the loop finishes, no path was found
        return None

    def display(self):
        print("--- Almacén ---")
        for fila in self.cuadricula:
            print(' '.join(fila))
        print("---------------")