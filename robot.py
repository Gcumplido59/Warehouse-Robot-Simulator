class Robot:
    """Represents the robot that navigates the warehouse.

    Attributes:
        row (int): The current row position of the robot on the grid.
        column (int): The current column position of the robot on the grid.
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def move_up(self):
        """Moves the robot one cell up."""
        self.row -= 1

    def move_down(self):
        """Moves the robot one cell down."""
        self.row += 1

    def move_left(self):
        """Moves the robot one cell to the left."""
        self.column -= 1

    def move_right(self):
        """Moves the robot one cell to the right."""
        self.column += 1