class Obstacle:
    """Represents an obstacle in the warehouse grid.

    Attributes:
        row (int): The row position of the obstacle on the grid.
        column (int): The column position of the obstacle on the grid.
    """
    def __init__(self, row, column):
        self.row = row
        self.column = column