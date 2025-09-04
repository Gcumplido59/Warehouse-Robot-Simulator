from collections import deque

class Warehouse:
    """Manages the state and logic of the warehouse grid.

    This class is responsible for creating the grid, placing the robot,
    package, and obstacles, and finding the shortest path between the
    robot and the package using the Breadth-First Search (BFS) algorithm.

    Attributes:
        width (int): The width of the warehouse grid.
        height (int): The height of the warehouse grid.
        robot (Robot): The robot object in the warehouse.
        package (Package): The package object in the warehouse.
        grid (list[list[str]]): A 2D list representing the grid layout.
    """
    def __init__(self, width, height):
        """Initializes the warehouse with a given width and height.

        Args:
            width (int): The number of columns in the grid.
            height (int): The number of rows in the grid.
        """
        self.width = width
        self.height = height
        self.robot = None
        self.package = None
        self.grid = [['0' for _ in range(width)] for _ in range(height)]

    def add_robot(self, robot_obj):
        """Adds a robot to the warehouse grid.

        Args:
            robot_obj (Robot): The robot instance to add.
        """
        self.robot = robot_obj
        self.grid[self.robot.row][self.robot.column] = 'R'

    def place_object(self, obj, symbol):
        """Places a generic object onto the grid.

        Args:
            obj (object): The object to place, must have `row` and `column` attributes.
            symbol (str): The character symbol to represent the object on the grid.
        """
        self.grid[obj.row][obj.column] = symbol

    def find_path(self):
        """Finds the shortest path from the robot to the package using BFS.

        The Breadth-First Search (BFS) algorithm explores the grid layer by
        layer from the robot's starting position. It guarantees finding the
        shortest path in an unweighted grid by checking all possible paths
        of a certain length before moving on to longer paths.

        The algorithm works as follows:
        1. Initialize a queue with the starting path (containing only the robot's position).
        2. Initialize a `visited` set to keep track of visited cells to avoid cycles.
        3. While the queue is not empty, dequeue the oldest path.
        4. Get the last position from the current path.
        5. If this position is the package's location, the path is found.
        6. Otherwise, explore all valid, unvisited neighbors (up, down, left, right).
        7. For each valid neighbor, create a new path by extending the current path,
           add it to the queue, and mark the neighbor as visited.
        8. If the queue becomes empty and the package has not been reached, no path exists.

        Returns:
            list[tuple[int, int]] or None: A list of (row, col) tuples representing
            the shortest path from the robot to the package. Returns None if no
            path is found.
        """
        if not self.robot or not self.package:
            print("Robot or package not in warehouse.")
            return None

        start_pos = (self.robot.row, self.robot.column)
        goal_pos = (self.package.row, self.package.column)

        queue = deque([[start_pos]])
        visited = {start_pos}

        while queue:
            current_path = queue.popleft()
            current_pos = current_path[-1]

            if current_pos == goal_pos:
                return current_path

            for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
                n_row, n_col = neighbor_pos

                if (0 <= n_row < self.height and
                    0 <= n_col < self.width and
                    self.grid[n_row][n_col] in ['0', '📦'] and
                    neighbor_pos not in visited):
                    
                    visited.add(neighbor_pos)
                    new_path = list(current_path)
                    new_path.append(neighbor_pos)
                    queue.append(new_path)
        return None

    def display_path(self, path):
        """Marks the found path on the grid for display.

        Args:
            path (list[tuple[int, int]]): The path to display.
        """
        for pos in path:
            row, col = pos
            if self.grid[row][col] == '0':
                self.grid[row][col] = '.'
        self.display()

    def reset(self):
        """Resets the warehouse grid to its initial state.

        Clears all obstacles and the package from the grid, leaving only
        the robot at its starting position.
        """
        self.package = None
        for r in range(self.height):
            for c in range(self.width):
                if (r, c) != (self.robot.row, self.robot.column):
                    self.grid[r][c] = '0'

    def add_package(self, package_obj=None, row=None, col=None):
        """Adds a package to the warehouse grid.

        This method can add a package either from a Package object or from
        row and column coordinates.

        Args:
            package_obj (Package, optional): The package instance to add.
            row (int, optional): The row position for the new package.
            col (int, optional): The column position for the new package.
        """
        if package_obj:
            self.package = package_obj
            self.grid[package_obj.row][package_obj.column] = '📦'
        elif row is not None and col is not None:
            from package import Package # Import locally to avoid unnecessary top-level import
            self.package = Package(row, col)
            self.grid[row][col] = '📦'

    def display(self):
        """Prints a text-based representation of the warehouse grid to the console."""
        print("--- Warehouse ---")
        for row in self.grid:
            print(' '.join(row))
        print("---------------")